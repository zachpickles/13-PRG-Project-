import tkinter as tk
import random

Questions = [
    "25% of 76",                    #MPC
    "18% of 200",                   #MPC
    "38% of 6200",                  #MPC
    "33.33% of $1200",              #MPC
    "1.25% of $3275",               #MPC
    "75% of $490",                  #MPC
    "15% of $1.60",                 #MPC
    "8% of $2",                     #MPC
    "66.66% of 930g",               #MPC
    "15% of 180",                   #MPC
    "is 118% of 450 = 531",         #TORF
    "is 115% of $40 = $50",         #TORF
    "is 200% of 450 = 900 ",        #TORF
    "is 108% of $13.50 = $16.58",   #TORF
    "is 72/480 in % = 15% ",        #TORF
    "is 13000 - 15% = 11050",       #TORF
    "is 425 - 4% = 400",            #TORF
    "is 450 - 85% = 65.5",          #TORF
    "is 24/20 in % = 120% ",        #TORF
    "is 13000/10400 in % = 130%"    #TORF
]
ButtonsText = [
    [
        "18", "19", "25"  #19
    ],
    [
        "36", "130", "30"  #36
    ],
    [
        "4329", "2300","2356"  #2356
    ],
    [
        "$380", "$500","$400"  #$400
    ],
    [
         "$41", "$40.94", "$40"  #$40.94
    ],
    [
        "$367.50", "$350", "$400"  #367.50
    ],
    [
        "24 cents", "50 cents", "$24"  #24 cents
    ],
    [
         "20 cents", "10", "16 cents"  #16 cents
    ],
    [
         "550g", "700g", "620g"  #620g
    ],
    [
         "30", "27", "50"  #27
    ],
    [
        "True", "False"  #True
    ],
    [
        "True", "False"  #false
    ],
    [
        "True", "False"  #True
    ],
    [
        "True", "False"  #False
    ],
    [
        "True", "False"  #True
    ],
    [
        "True", "False"  #True
    ],
    [
        "True", "False"  #False
    ],
    [
        "True", "False"  #False
    ],
    [
        "True", "False"  #True
    ],
    [
        "True", "False"  #False
    ],
]

Answers = [
    "b",
    "a",
    "a",
    "c",
    "b",
    "a",
    "a",
    "c",
    "c",
    "b",
    "true",
    "false",
    "true",
    "false",
    "true",
    "true",
    "false",
    "false",
    "true",
    "false"
]


Shuffle1 = list(zip(Questions, Answers, ButtonsText))
random.shuffle(Shuffle1)
Questions, Answers, ButtonsText = zip(*Shuffle1)

Correct = 0
skips = 0
i = 1


class StartScreen():
    def __init__(self):
        global Questions
        global Answers
        global ButtonsText
        global i
        global Correct
        global skips
        Correct = 0
        skips = 0
        i = 1
        ButtonPressed = False
        Shuffle1 = list(zip(Questions, Answers, ButtonsText))
        random.shuffle(Shuffle1)
        Questions, Answers, ButtonsText = zip(*Shuffle1)

        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.configure(bg='#cfe2f3')
        self.root.title("Percentages Math Quiz")
        Title = tk.Label(self.root, text="PERCENTAGES MATH QUIZ", bg="#cceae3", font="Arial 18",width=28,height=3 ,borderwidth=1, relief="solid").place(x=225, y=80)
        Quit = tk.Button(self.root,
                           text = 'QUIT', borderwidth=1, relief="solid", bg="#cceae3", width=15, height=2, font="Arial 14",
                           command = lambda : self.quit()).place(x=610, y=425)
        Start = tk.Button(self.root,
                            text = "START", borderwidth=1, relief="solid", bg="#cceae3", width=20, height=3, font="Arial 14",
                            command = lambda : self.Starts()).place(x=320, y=200)
        InstTitle = tk.Label()
        Inst = tk.Label()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()

    def Starts(self):
        self.root.destroy()
        second = Question()


class Question():

    def __init__(self):
        global Correct
        global skips
        global i
        global ButtonPressed
        while i < 11 + skips:
            if len(ButtonsText[i]) == 3:
                ButtonPressed = False
                self.Setup3btn(Questions[i], ButtonsText[i][0], ButtonsText[i][1], ButtonsText[i][2], Answers[i], i)
            elif len(ButtonsText[i]) == 2:
                ButtonPressed = False
                self.Setup2btn(Questions[i], ButtonsText[i][0], ButtonsText[i][1], Answers[i], i)
            else:
                quit()
        third = FinalScreen()


    def Setup3btn(self, Question, ButtonOne, ButtonTwo, ButtonThree, Answer, LCV):
        global skips
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.configure(bg='#cfe2f3')
        self.root.title("Percentages Math Quiz")
        QuestNum = tk.Label(self.root, text="Question " + str(LCV - skips) + "/10", bg="#cceae3", font="Arial 14", width=15,
                            height=2, borderwidth=1, relief="solid").place(x=5, y=5)
        Quest = tk.Label(self.root, text=Question, bg="#cceae3", font="Arial 18", width=28, height=3, borderwidth=1,
                         relief="solid").place(x=210, y=150)

        ButtonA = tk.Button(self.root,
                            text=str(ButtonOne), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "a")).place(x=260, y=260)

        ButtonB = tk.Button(self.root,
                            text=str(ButtonTwo), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "b")).place(x=360, y=260)

        ButtonC = tk.Button(self.root,
                            text=str(ButtonThree), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "c")).place(x=460, y=260)
        SkipButton = tk.Button(self.root,
                               text="Skip Question", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                               width=12, height=1,
                               command=lambda: self.Skip()).place(x=640, y=450)
        if ButtonPressed == True:
            return
        else:
            self.root.mainloop()
        return



    def Setup2btn(self, Question, Button1, Button2, Answer, LCV):
        global skips
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.configure(bg='#cfe2f3')
        self.root.title("Percentages Math Quiz")
        QuestNum = tk.Label(self.root, text="Question " + str(LCV - skips) + "/10", bg="#cceae3", font="Arial 14", width=15,
                            height=2, borderwidth=1, relief="solid").place(x=5, y=5)
        Quest = tk.Label(self.root, text=Question, bg="#cceae3", font="Arial 18", width=28, height=3, borderwidth=1,
                         relief="solid").place(x=210, y=150)

        ButtonA = tk.Button(self.root,
                            text=str(Button1), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "true")).place(x=320, y=260)

        ButtonB = tk.Button(self.root,
                            text=str(Button2), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "false")).place(x=420, y=260)

        SkipButton = tk.Button(self.root,
                               text="Skip Question", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                               width=12, height=1,
                               command=lambda: self.Skip()).place(x=640, y=450)
        if ButtonPressed == True:
            return
        else:
            self.root.mainloop()
        return



    def Buttons(self, Answer, ButtonTypes):
        global ButtonPressed
        if Answer == ButtonTypes:
            ButtonPressed = True
            global Correct
            global i
            Correct = Correct + 1
            i = i + 1
        elif Answer != ButtonTypes:
            i = i + 1
            ButtonPressed = True
        self.root.destroy()
        second = Question()
        return


    def Skip(self):
        global ButtonPressed
        ButtonPressed = True
        global skips
        global i
        if skips < 3:
            skips = skips + 1
            i = i + 1
            self.root.destroy()
            second = Question()
            return
        else:
            ButtonPressed = False
            return

class FinalScreen():
    def __init__(self):

        global Correct
        percents = Correct/10
        if percents < 0.5:
            Grade = "N/A"
        elif percents > 0.49 and percents < 0.7:
            Grade = "A"
        elif percents > 0.69 and percents < 0.9:
            Grade = "M"
        elif percents > 0.89 and percents < 1.01:
            Grade = "E"
        else:
            quit()
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.configure(bg='#cfe2f3')
        self.root.title("Percentages Math Quiz")

        Title = tk.Label(self.root, text="Results", bg="#cceae3", font="Arial 18", width=15,
                         height=2, borderwidth=1, relief="solid").place(x=330, y=120)
        Result = tk.Label(self.root, text=Grade + "\n" + "You Got: " + str(Correct) + "/10", bg="#cceae3", font="Arial 20",
                          width=20,
                          height=5, borderwidth=1, relief="solid").place(x=270, y=200)

        TryAgn = tk.Button(self.root, text="TRY AGAIN", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                           width=12, height=1,
                           command=lambda: self.tryAgain()).place(x=640, y=450)

        QuitButton = tk.Button(self.root, text="QUIT", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                               width=12, height=1, command=lambda: quit()).place(x=10, y=450)

        self.root.mainloop()

    def tryAgain(self):
        self.root.destroy()
        StartScreen()
        
app = StartScreen()
