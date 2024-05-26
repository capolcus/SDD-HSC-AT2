import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk

systemsInfo = {
    'Skeletal System': {
        'image': 'skeletal_system.png',
        'parts': [
            "Skull", "Vertebrae", "Clavicle", "Ribs", "Sternum", "Humerus", 
            "Radius", "Ulna", "Pelvis", "Carpals", "Femur", "Patella", 
            "Fibula", "Tibia", "Tarsals"
        ],
        'info': {
            "Skull": "The skull is composed of 22 bones, including the cranium and the facial bones. It protects the brain and forms the structure of the face.",
            "Vertebrae": "The vertebrae are a series of 33 bones forming the spinal column. They protect the spinal cord and support the head and body. They are divided into cervical, thoracic, lumbar, sacral, and coccygeal regions.",
            "Clavicle": "Also known as the collarbone, the clavicle connects the arm to the body, spanning between the sternum and the scapula. It provides structural support and stability to the shoulder.",
            "Ribs": "There are 24 ribs in the human body, 12 on each side. They protect the thoracic cavity and support the chest wall. The first seven pairs are true ribs, attaching directly to the sternum, while the next three pairs are false ribs, and the last two pairs are floating ribs.",
            "Sternum": "The sternum, or breastbone, is a long, flat bone located in the center of the chest. It connects to the ribs via cartilage, forming the front of the rib cage and protecting vital organs.",
            "Humerus": "The humerus is the upper arm bone, extending from the shoulder to the elbow. It articulates with the scapula at the shoulder and the radius and ulna at the elbow.",
            "Radius": "The radius is one of the two long bones in the forearm, located on the lateral side (thumb side). It works with the ulna to enable forearm movement.",
            "Ulna": "The ulna is the other long bone in the forearm, located on the medial side (pinky side). It is larger and longer than the radius and forms the elbow joint with the humerus.",
            "Pelvis": "The pelvis is a ring of bones connecting the spine to the femurs. It supports the weight of the upper body, protects pelvic organs, and serves as the attachment point for lower limb muscles.",
            "Carpals": "The carpal bones are eight small bones in the wrist, arranged in two rows. They facilitate the complex movements of the wrist and hand.",
            "Femur": "The femur, or thigh bone, is the longest and strongest bone in the body. It extends from the hip to the knee, supporting the weight of the body and enabling leg movement.",
            "Patella": "The patella, or kneecap, is a small, triangular bone that protects the knee joint and improves the leverage of the thigh muscles.",
            "Fibula": "The fibula is the smaller of the two bones in the lower leg, running parallel to the tibia. It stabilizes the ankle and supports lower leg muscles.",
            "Tibia": "The tibia, or shinbone, is the larger and stronger of the two lower leg bones. It bears most of the body's weight and forms the lower part of the knee joint and the inner part of the ankle joint.",
            "Tarsals": "The tarsal bones are a group of seven bones in the ankle. They support body weight and enable foot movement."
        }
    },
    'Muscular System': {
        'image': 'muscular_system.png',
        'parts': [
            "Trapezius", "Deltoid", "Biceps", "Triceps", "Chest", 
            "Abdominals", "Groin", "Quadriceps", "Latissimus", 
            "Glutes", "Hamstrings", "Calves", "Achilles"
        ],
        'info': {
            "Trapezius": "The trapezius is a large, triangular muscle located on the upper back and neck. It helps move the scapulae and supports the arm. It also extends the neck.",
            "Deltoid": "The deltoid is the rounded muscle covering the shoulder. It is responsible for lifting the arm and giving the shoulder its range of motion.",
            "Chest": "The pectoralis major is a thick, fan-shaped muscle situated at the chest. It helps in flexion, adduction, and rotation of the humerus.",
            "Biceps": "The bicep is a two-headed muscle located on the front of the upper arm. It is responsible for flexion and supination of the forearm.",
            "Triceps": "The triceps is a three-headed muscle located on the back of the upper arm. It is responsible for extending the forearm.",
            "Latissimus": "The latissimus dorsi is a broad, flat muscle on the back that stretches to the sides. It is involved in movements of the shoulder joint, including extension, adduction, and internal rotation.",
            "Abdominals": "The abdominal muscles include the rectus abdominis, obliques, and transversus abdominis. They are responsible for flexing the spine, stabilizing the core, and aiding in breathing.",
            "Groin": "The adductor muscles are located on the inner thigh. They are responsible for adducting the thigh, bringing the legs together.",
            "Quadriceps": "The quadriceps are a group of four muscles on the front of the thigh. They are responsible for extending the knee and flexing the hip.",
            "Hamstrings": "The hamstrings are a group of three muscles on the back of the thigh. They are responsible for flexing the knee and extending the hip.",
            "Glutes": "The gluteal muscles include the gluteus maximus, medius, and minimus. They are responsible for the movement of the hip and thigh, including extension, abduction, and rotation.",
            "Calves": "The calf muscles include the gastrocnemius and soleus. They are responsible for plantar flexion of the foot and flexion of the knee.",
            "Achilles": "The Achilles tendon is a tough band of fibrous tissue connecting the calf muscles to the heel bone. It allows for walking, running, and jumping by enabling plantar flexion of the foot."
        }
    }
}

quizData = {
    'Skeletal Quiz': [
        {'question': "Which bone is the longest in the human body?", 'options': ['Skull', 'Femur', 'Humerus'], 'answer': 'Femur'},
        {'question': "Which bone protects the brain?", 'options': ['Skull', 'Vertebrae', 'Clavicle'], 'answer': 'Skull'},
        {'question': "How many vertebrae are in the human spine?", 'options': ['33', '24', '12'], 'answer': '33'},
        {'question': "What is the common name for the clavicle?", 'options': ['Collarbone', 'Shoulder blade', 'Kneecap'], 'answer': 'Collarbone'},
        {'question': "How many ribs are in the human body?", 'options': ['24', '12', '18'], 'answer': '24'},
        {'question': "Which bone is known as the breastbone?", 'options': ['Sternum', 'Ribs', 'Pelvis'], 'answer': 'Sternum'},
        {'question': "Which bone is the upper arm bone?", 'options': ['Humerus', 'Radius', 'Ulna'], 'answer': 'Humerus'},
        {'question': "Which bone is on the thumb side of the forearm?", 'options': ['Radius', 'Ulna', 'Humerus'], 'answer': 'Radius'},
        {'question': "Which bone is on the pinky side of the forearm?", 'options': ['Ulna', 'Radius', 'Tibia'], 'answer': 'Ulna'},
        {'question': "Which bone connects the spine to the femurs?", 'options': ['Pelvis', 'Tarsals', 'Carpals'], 'answer': 'Pelvis'},
        {'question': "How many carpal bones are in the wrist?", 'options': ['8', '7', '6'], 'answer': '8'},
        {'question': "Which bone is the thigh bone?", 'options': ['Femur', 'Tibia', 'Fibula'], 'answer': 'Femur'},
        {'question': "What is the common name for the patella?", 'options': ['Kneecap', 'Shinbone', 'Collarbone'], 'answer': 'Kneecap'},
        {'question': "Which bone stabilizes the ankle?", 'options': ['Fibula', 'Tibia', 'Femur'], 'answer': 'Fibula'},
        {'question': "Which bone is known as the shinbone?", 'options': ['Tibia', 'Fibula', 'Femur'], 'answer': 'Tibia'},
        {'question': "How many tarsal bones are in the ankle?", 'options': ['7', '8', '6'], 'answer': '7'}
    ],
    'Muscular Quiz': [
        {'question': "Which muscle is known for extending the neck?", 'options': ['Trapezius', 'Deltoid', 'Biceps'], 'answer': 'Trapezius'},
        {'question': "Which muscle covers the shoulder?", 'options': ['Deltoid', 'Trapezius', 'Chest'], 'answer': 'Deltoid'},
        {'question': "Which muscle is located at the chest?", 'options': ['Chest', 'Biceps', 'Triceps'], 'answer': 'Chest'},
        {'question': "Which muscle is located on the front of the upper arm?", 'options': ['Biceps', 'Triceps', 'Latissimus'], 'answer': 'Biceps'},
        {'question': "Which muscle is located on the back of the upper arm?", 'options': ['Triceps', 'Biceps', 'Deltoid'], 'answer': 'Triceps'},
        {'question': "Which muscle is a broad, flat muscle on the back?", 'options': ['Latissimus', 'Abdominals', 'Groin'], 'answer': 'Latissimus'},
        {'question': "Which muscles include the rectus abdominis, obliques, and transversus abdominis?", 'options': ['Abdominals', 'Quadriceps', 'Hamstrings'], 'answer': 'Abdominals'},
        {'question': "Which muscles are located on the inner thigh?", 'options': ['Groin', 'Quadriceps', 'Glutes'], 'answer': 'Groin'},
        {'question': "Which muscle group is on the front of the thigh?", 'options': ['Quadriceps', 'Hamstrings', 'Calves'], 'answer': 'Quadriceps'},
        {'question': "Which muscle group is on the back of the thigh?", 'options': ['Hamstrings', 'Quadriceps', 'Calves'], 'answer': 'Hamstrings'},
        {'question': "Which muscles include the gluteus maximus, medius, and minimus?", 'options': ['Glutes', 'Hamstrings', 'Groin'], 'answer': 'Glutes'},
        {'question': "Which muscles include the gastrocnemius and soleus?", 'options': ['Calves', 'Hamstrings', 'Quadriceps'], 'answer': 'Calves'},
        {'question': "Which tendon connects the calf muscles to the heel bone?", 'options': ['Achilles', 'Quadriceps', 'Hamstrings'], 'answer': 'Achilles'}
    ]
}

userProgress = {'Skeletal Score': [], 'Muscular Score': []}

class AnatomyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ashu's Anatomy")
        self.geometry("1200x800")
        self.theme = "Red"
        self.textSize = 16
        self.configureTheme()
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.mainMenu()

    def configureTheme(self):
        themes = {
            "Red": {"bg": "black", "textColor": "white", "buttonFgColor": "red", "buttonHoverColor": "darkred"},
            "Blue": {"bg": "#2E3440", "textColor": "#D8DEE9", "buttonFgColor": "#5E81AC", "buttonHoverColor": "#4C6789"},
            "Green": {"bg": "#1D1F21", "textColor": "#C5C8C6", "buttonFgColor": "#A3BE8C", "buttonHoverColor": "#8FBC8B"},
            "Purple": {"bg": "#282A36", "textColor": "#F8F8F2", "buttonFgColor": "#BD93F9", "buttonHoverColor": "#B48EAD"},
            "Orange": {"bg": "#282828", "textColor": "#EBDBB2", "buttonFgColor": "#FE8019", "buttonHoverColor": "#D65D0E"},
            "Yellow": {"bg": "#002B36", "textColor": "#839496", "buttonFgColor": "#FABD2F", "buttonHoverColor": "#D79921"}
        }

        theme = themes[self.theme]
        self.configure(bg=theme["bg"])
        self.textColor = theme["textColor"]
        self.buttonFgColor = theme["buttonFgColor"]
        self.buttonHoverColor = theme["buttonHoverColor"]

    def clearWindow(self):
        for widget in self.winfo_children():
            widget.destroy()

    def mainMenu(self):
        self.clearWindow()
        container = ctk.CTkFrame(self, fg_color=self['bg'])
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        title = ctk.CTkLabel(container, text="Ashu's Anatomy", font=("Helvetica", 24, "bold"), fg_color=self['bg'], text_color=self.textColor)
        title.grid(row=0, column=0, pady=20)
        buttons = [
            ("Learning ", self.learn),
            ("Quizzes", self.quiz),
            ("Progress Tracker", self.showProgress),
            ("Settings", self.settings),
            ("Exit", self.quit)
        ]
        for idx, (text, command) in enumerate(buttons):
            button = ctk.CTkButton(container, text=text, command=command, width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
            button.grid(row=idx + 1, column=0, pady=10, sticky="ew")

    def learn(self):
        self.clearWindow()
        container = ctk.CTkFrame(self, fg_color=self['bg'])
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        title = ctk.CTkLabel(container, text="Skeletal or Muscular System", font=("Helvetica", 24, "bold"), fg_color=self['bg'], text_color=self.textColor)
        title.grid(row=0, column=0, pady=20)
        systems = list(systemsInfo.keys())
        for idx, system in enumerate(systems):
            button = ctk.CTkButton(container, text=system, command=lambda s=system: self.showSystemInfo(s), width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
            button.grid(row=idx + 1, column=0, pady=10, sticky="ew")
        backButton = ctk.CTkButton(self, text="Back", command=self.mainMenu, width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
        backButton.grid(row=2, column=1, padx=20, pady=20, sticky="se")

    def showSystemInfo(self, system):
        self.clearWindow()
        container = ctk.CTkFrame(self, fg_color=self['bg'])
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=1)
        systemData = systemsInfo[system]
        imagePath = systemData['image']
        parts = systemData['parts']
        info = systemData['info']
        title = ctk.CTkLabel(container, text=system, font=("Helvetica", 24, "bold"), fg_color=self['bg'], text_color=self.textColor)
        title.grid(row=0, column=0, columnspan=2, pady=20)
        
        frame = tk.Frame(container, bg='white')
        frame.grid(row=1, column=0, pady=10, padx=10)
        
        img = tk.PhotoImage(file=imagePath)
        
        canvas = tk.Canvas(frame, bg='white', width=img.width(), height=img.height(), highlightthickness=0)
        canvas.create_image(img.width()//2, img.height()//2, anchor=tk.CENTER, image=img)
        canvas.image = img
        canvas.pack()

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground=self['bg'], background=self.buttonFgColor, foreground=self.textColor, selectbackground=self.buttonHoverColor, selectforeground=self['bg'], font=("Helvetica", self.textSize))
        style.map('TCombobox', fieldbackground=[('readonly', self.buttonFgColor)], background=[('readonly', self.buttonFgColor)], foreground=[('readonly', self.textColor)], selectbackground=[('readonly', self.buttonHoverColor)], selectforeground=[('readonly', self['bg'])])

        infoTextbox = tk.Text(container, font=("Helvetica", self.textSize), bg=self['bg'], fg=self.textColor, wrap="word", height=10, width=40)
        infoTextbox.grid(row=1, column=1, pady=(5, 5), padx=10, sticky="n")
        infoTextbox.configure(state='disabled')

        partsCombobox = ttk.Combobox(container, font=("Helvetica", self.textSize), values=parts, style="TCombobox", width=30)
        partsCombobox.grid(row=2, column=1, pady=5, padx=10, sticky="n")
        partsCombobox.set("Select a part")

        def onPartSelect(event):
            selectedPart = partsCombobox.get()
            infoTextbox.configure(state='normal')
            infoTextbox.delete('1.0', tk.END)
            infoTextbox.insert(tk.END, info[selectedPart])
            infoTextbox.configure(state='disabled')

        partsCombobox.bind("<<ComboboxSelected>>", onPartSelect)
        
        backButton = ctk.CTkButton(container, text="Back", command=self.learn, width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
        backButton.grid(row=3, column=1, padx=20, pady=20, sticky="se")

    def quiz(self):
        self.clearWindow()
        self.quizContainer = ctk.CTkFrame(self, fg_color=self['bg'])
        self.quizContainer.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.quizContainer.grid_columnconfigure(0, weight=1)
        title = ctk.CTkLabel(self.quizContainer, text="Select Quiz", font=("Helvetica", 24, "bold"), fg_color=self['bg'], text_color=self.textColor)
        title.grid(row=0, column=0, pady=20)
        quizzes = quizData.keys()
        for idx, system in enumerate(quizzes):
            button = ctk.CTkButton(self.quizContainer, text=system, command=lambda s=system: self.takeQuiz(s), width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
            button.grid(row=idx + 1, column=0, pady=10, sticky="ew")
        backButton = ctk.CTkButton(self, text="Back", command=self.mainMenu, width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
        backButton.grid(row=2, column=1, padx=20, pady=20, sticky="se")

    def takeQuiz(self, system):
        self.clearWindow()
        self.quizContainer = ctk.CTkFrame(self, fg_color=self['bg'])
        self.quizContainer.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.quizContainer.grid_columnconfigure(0, weight=1)
        questions = quizData[system]
        self.score = 0
        self.questionIndex = 0
        self.totalQuestions = len(questions)
        self.questions = questions
        self.currentSystem = system

        self.showQuestion()

    def showQuestion(self):
        if self.questionIndex < self.totalQuestions:
            questionData = self.questions[self.questionIndex]
            questionFrame = QuestionFrame(self.quizContainer, questionData, self.checkAnswer, self.textColor, self.buttonFgColor, self.buttonHoverColor, self.textSize)
            questionFrame.grid(row=0, column=0, pady=20)
        else:
            self.displayScore()

    def checkAnswer(self, selectedOption):
        if selectedOption == self.questions[self.questionIndex]['answer']:
            self.score += 1
        self.questionIndex += 1
        self.showQuestion()

    def displayScore(self):
        userProgress[self.currentSystem].append(self.score)
        self.clearWindow()
        container = ctk.CTkFrame(self, fg_color=self['bg'])
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        scoreLabel = ctk.CTkLabel(container, text=f"You scored {self.score}/{self.totalQuestions}", font=("Helvetica", 24, "bold"), fg_color=self['bg'], text_color=self.textColor)
        scoreLabel.grid(row=0, column=0, pady=20)
        backButton = ctk.CTkButton(container, text="Back", command=self.mainMenu, width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
        backButton.grid(row=1, column=0, pady=20, sticky="n")

    def showProgress(self):
        self.clearWindow()
        container = ctk.CTkFrame(self, fg_color=self['bg'])
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        title = ctk.CTkLabel(container, text="Progress", font=("Helvetica", 24, "bold"), fg_color=self['bg'], text_color=self.textColor)
        title.grid(row=0, column=0, pady=20)
        for idx, (system, scores) in enumerate(userProgress.items()):
            label = ctk.CTkLabel(container, text=f"{system}:", font=("Helvetica", 16), fg_color=self['bg'], text_color=self.textColor)
            label.grid(row=idx * 2 + 1, column=0, pady=10)
            for scoreIdx, score in enumerate(scores):
                scoreLabel = ctk.CTkLabel(container, text=f"Attempt {scoreIdx + 1}: {score}", font=("Helvetica", 14), fg_color=self['bg'], text_color=self.textColor)
                scoreLabel.grid(row=idx * 2 + 2, column=0, pady=5)
        backButton = ctk.CTkButton(self, text="Back", command=self.mainMenu, width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
        backButton.grid(row=2, column=1, padx=20, pady=20, sticky="se")

    def settings(self):
        self.clearWindow()
        container = ctk.CTkFrame(self, fg_color=self['bg'])
        container.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        container.grid_columnconfigure(0, weight=1)
        title = ctk.CTkLabel(container, text="Settings", font=("Helvetica", 24, "bold"), fg_color=self['bg'], text_color=self.textColor)
        title.grid(row=0, column=0, pady=20)

        def applyTheme():
            selectedTheme = themeVar.get()
            self.theme = selectedTheme
            self.configureTheme()
            self.mainMenu()

        def applyTextSize():
            selectedSize = sizeVar.get()
            self.textSize = int(selectedSize)
            self.configureTheme()
            self.mainMenu()

        themeVar = tk.StringVar(value=self.theme)
        themeLabel = ctk.CTkLabel(container, text="Select Theme:", font=("Helvetica", 16), fg_color=self['bg'], text_color=self.textColor)
        themeLabel.grid(row=1, column=0, pady=10)
        themeOptions = ["Red", "Blue", "Green", "Purple", "Orange", "Yellow"]
        themeMenu = ctk.CTkOptionMenu(container, variable=themeVar, values=themeOptions, fg_color=self.buttonFgColor, text_color=self['bg'])
        themeMenu.grid(row=1, column=1, pady=10)

        sizeLabel = ctk.CTkLabel(container, text="Select Text Size:", font=("Helvetica", 16), fg_color=self['bg'], text_color=self.textColor)
        sizeLabel.grid(row=2, column=0, pady=10)
        sizeVar = tk.StringVar(value=str(self.textSize))
        sizeMenu = ctk.CTkOptionMenu(container, variable=sizeVar, values=["12", "14", "16", "18", "20"], fg_color=self.buttonFgColor, text_color=self['bg'])
        sizeMenu.grid(row=2, column=1, pady=10)
        sizeButton = ctk.CTkButton(container, text="Apply Text Size", command=applyTextSize, width=100, height=30, font=("Helvetica", 14), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
        sizeButton.grid(row=3, column=0, columnspan=2, pady=10)

        themeButton = ctk.CTkButton(container, text="Apply Theme", command=applyTheme, width=100, height=30, font=("Helvetica", 14), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
        themeButton.grid(row=4, column=0, columnspan=2, pady=10)

        backButton = ctk.CTkButton(self, text="Back", command=self.mainMenu, width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
        backButton.grid(row=5, column=1, padx=20, pady=20, sticky="se")

class QuestionFrame(ctk.CTkFrame):
    def __init__(self, master, questionData, checkAnswerCallback, textColor, buttonFgColor, buttonHoverColor, textSize):
        super().__init__(master, fg_color=master['bg'])
        self.questionData = questionData
        self.checkAnswerCallback = checkAnswerCallback
        self.textColor = textColor
        self.buttonFgColor = buttonFgColor
        self.buttonHoverColor = buttonHoverColor
        self.textSize = textSize
        self.grid_columnconfigure(0, weight=1)
        self.createWidgets()

    def createWidgets(self):
        questionLabel = ctk.CTkLabel(self, text=self.questionData['question'], font=("Helvetica", 18), fg_color=self['bg'], text_color=self.textColor)
        questionLabel.grid(row=0, column=0, pady=10)
        for idx, option in enumerate(self.questionData['options']):
            button = ctk.CTkButton(self, text=option, command=lambda opt=option: self.checkAnswer(opt), width=200, height=40, font=("Helvetica", self.textSize), fg_color=self.buttonFgColor, hover_color=self.buttonHoverColor, text_color=self['bg'])
            button.grid(row=idx + 1, column=0, pady=5)

    def checkAnswer(self, selectedOption):
        self.destroy()
        self.checkAnswerCallback(selectedOption)

if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")
    app = AnatomyApp()
    app.mainloop()
