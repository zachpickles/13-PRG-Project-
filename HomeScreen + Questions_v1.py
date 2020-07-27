import tkinter as tk
import random

Questions = [
    "25% of 76",
    "18% of 200",
    "38% of 6200",
    "33.33% of $1200",
    "1.25% of $3275",
    "75% of $490",
    "15% of $1.60",
    "8% of $2",
    "66.66% of 930g",
    "15% of 180",
    "118% of 450",
    "115%of $40",
    "200% of 450 ",
    "108% of $13.50",
    "72/480 in % ",
    "13000 - 15%",
    "425 - 4%",
    "450 - 85%",
    "24/20 in % ",
    "13000/10400 in %"
]
ButtonsText = [
    [
        "18", "19", "25" #19
    ],
    [
        "36", "130", "30" #36
    ],
    [
        "4329", "2300","2356" #2356
    ],
    [
        "$380", "$500","$400"  #$400
    ],
    [
         "$41", "$40.94", "$40" #$40.94
    ],
    [
        "$367.50", "$350", "$400" #367.50
    ],
    [
        "24 cents", "50 cents", "$24" #24 cents
    ],
    [
         "20 cents", "10", "16 cents" #16 cents
    ],
    [
         "550g", "700g", "620g" #620g
    ],
    [
         "30", "27", "50" #27
    ],
    [
        "True", "False" #True
    ],
    [
        "True", "False" #false
    ],
    [
        "True", "False" #True
    ],
    [
        "True", "False" #False
    ],
    [
        "True", "False" #True
    ],
    [
        "True", "False" #True
    ],
    [
        "True", "False" #False
    ],
    [
        "True", "False" #False
    ],
    [
        "True", "False" #True
    ],
    [
        "True", "False" #False
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



class StartScreen():
    def __init__(self):
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
        i = 0
        global Correct
        Correct = 0
        global skips
        skips = 0
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.configure(bg='#cfe2f3')
        self.root.title("Percentages Math Quiz")
        while i < 10:
            if len(ButtonsText[i]) == 3:
                self.Setup3btn(Questions[i], ButtonsText[i][0], ButtonsText[i][1], ButtonsText[i][2], Answers[i], i)
                i = i + 1
            elif len(ButtonsText[i]) == 2:
                self.Setup2btn(Questions[i], ButtonsText[i][0], ButtonsText[i][1], Answers[i], i)
                i = i + 1
            else:
                quit()
        quit()



    def Setup3btn(self, Question, ButtonOne, ButtonTwo, ButtonThree, Answer, LCV):
        print(Question, ButtonOne, ButtonTwo, ButtonThree, Answer, LCV)




    def Setup2btn(self, Question, Button1, Button2, Answer, LCV):
        print(Question, Button1, Button2, Answer, LCV)




app = StartScreen()








