import tkinter as tk    #imports tkinter package
import random   #imports random package 

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


Shuffle1 = list(zip(Questions, Answers, ButtonsText))   #Creates a variable containing all three lists
random.shuffle(Shuffle1)    #Shuffles the variable with the lists 
Questions, Answers, ButtonsText = zip(*Shuffle1)    #redifines the lists 

Correct = 0     #Declares Correct Variable to be global 
skips = 0   #Declares Skips Variable to be global 
i = 1   #Declares i Variable to be global 


class StartScreen():    #Declares Questions class 
    def __init__(self):     #Initialises Output (First function to always run)
        global Questions    #Calls Questions
        global Answers      #Calls Answers
        global ButtonsText  #Calls ButtonsText 
        global i        #Calls i
        global Correct  #Calls Correct
        global skips    #Calls skips
        Correct = 0     #defines Correct
        skips = 0       #defines skips
        i = 1       #defines i
        ButtonPressed = False   #defines ButtonPressed

        self.root = tk.Tk()     #initialises window 
        self.root.geometry('800x500')       #sets window size
        self.root.configure(bg='#cfe2f3')       #sets window colour
        self.root.title("Percentages Math Quiz")        #sets window name
        Title = tk.Label(self.root, text="PERCENTAGES MATH QUIZ", bg="#cceae3", font="Arial 18",width=28,height=3 ,borderwidth=1, relief="solid").place(x=225, y=80)    #initialises Title text
        Quit = tk.Button(self.root,
                           text = 'QUIT', borderwidth=1, relief="solid", bg="#cceae3", width=15, height=2, font="Arial 14",
                           command = lambda : quit()).place(x=610, y=425)   #Initialises quit button
        Start = tk.Button(self.root,
                            text = "START", borderwidth=1, relief="solid", bg="#cceae3", width=20, height=3, font="Arial 14",
                            command = lambda : self.Starts()).place(x=320, y=200)   #Initialises start button
        InstTitle = tk.Label(self.root, text="INSTRUCTIONS", bg="#cceae3", font="Arial 14",width=15,height=2 ,borderwidth=1, relief="solid").place(x=10, y=340)         #prints Instructions title
        Inst = tk.Label(self.root, text="This will be a 10 question quiz made\nup of true/false and multiple choice\nquestions. You will be given a NCEA grade.\nYou can only skip 3 times", bg="#cceae3", font="Arial 12",width=35,height=5,borderwidth=1, relief="solid").place(x=10, y=390)  #prints Instructions
        self.root.mainloop()    #loops window

    def Starts(self):   #start button function
        self.root.destroy()     #destroys window
        second = Question()     #goes to questions class


class Question():   #start of questions class

    def __init__(self):     #initialiser function
        global Correct      #calls Correct 
        global skips        #calls skips
        global i            #calls i
        global ButtonPressed    #calls ButtonPressed
        while i < 11 + skips:   #start of question loop
            if len(ButtonsText[i]) == 3:    #checks if multiple choice question
                ButtonPressed = False       #resets buttons
                self.Setup3btn(Questions[i], ButtonsText[i][0], ButtonsText[i][1], ButtonsText[i][2], Answers[i], i)    #calls setup for multiple choice questions
            elif len(ButtonsText[i]) == 2:      #checks if true or false question
                ButtonPressed = False       #resets buttons
                self.Setup2btn(Questions[i], ButtonsText[i][0], ButtonsText[i][1], Answers[i], i)       #calls setup for true or false questions
            else:   #error handling
                quit()      #quits if encounters an error
        third = FinalScreen()   #goes to results screen class


    def Setup3btn(self, Question, ButtonOne, ButtonTwo, ButtonThree, Answer, LCV):      #Start of multiple choice screen 
        global skips    #Calls skips
        self.root = tk.Tk()     #initialises window
        self.root.geometry('800x500')   #sets window size
        self.root.configure(bg='#cfe2f3')       #sets background colour
        self.root.title("Percentages Math Quiz")    #sets window title 
        QuestNum = tk.Label(self.root, text="Question " + str(LCV - skips) + "/10", bg="#cceae3", font="Arial 14", width=15,
                            height=2, borderwidth=1, relief="solid").place(x=5, y=5)    #prints which question the user is on
        Quest = tk.Label(self.root, text=Question, bg="#cceae3", font="Arial 18", width=28, height=3, borderwidth=1,
                         relief="solid").place(x=210, y=150)    #prints question

        ButtonA = tk.Button(self.root,
                            text=str(ButtonOne), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "a")).place(x=260, y=260)  #initialises Button a

        ButtonB = tk.Button(self.root,
                            text=str(ButtonTwo), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "b")).place(x=360, y=260)  #initialises button b 

        ButtonC = tk.Button(self.root,
                            text=str(ButtonThree), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "c")).place(x=460, y=260)  #initalises button c
        SkipButton = tk.Button(self.root,
                               text="Skip Question", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                               width=12, height=1,
                               command=lambda: self.Skip()).place(x=640, y=450)     #initialises skip button
        if ButtonPressed == True:   #checks if an option has been selected
            return  #returns to loop
        else:   #checks if button has been selected
            self.root.mainloop()    #loops window again
        return  #returns to loop



    def Setup2btn(self, Question, Button1, Button2, Answer, LCV):   #start of true or false window 
        global skips    #calls skips
        self.root = tk.Tk()     #initialises window
        self.root.geometry('800x500')   #sets window size
        self.root.configure(bg='#cfe2f3')   #sets background colour
        self.root.title("Percentages Math Quiz")    #sets window title
        QuestNum = tk.Label(self.root, text="Question " + str(LCV - skips) + "/10", bg="#cceae3", font="Arial 14", width=15,
                            height=2, borderwidth=1, relief="solid").place(x=5, y=5)    #prints question number
        Quest = tk.Label(self.root, text=Question, bg="#cceae3", font="Arial 18", width=28, height=3, borderwidth=1,
                         relief="solid").place(x=210, y=150)    #prints question

        ButtonA = tk.Button(self.root,
                            text=str(Button1), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "true")).place(x=320, y=260)   #initialises button a

        ButtonB = tk.Button(self.root,
                            text=str(Button2), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.Buttons(Answer, "false")).place(x=420, y=260)  #initialises button b 

        SkipButton = tk.Button(self.root,
                               text="Skip Question", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                               width=12, height=1,
                               command=lambda: self.Skip()).place(x=640, y=450)     #initialises skip button
        if ButtonPressed == True:   #checks if a button has been pressed
            return  #returns to loop
        else:   #checks if a button hasnt been pressed
            self.root.mainloop()    #loops window
        return  #returns to loop



    def Buttons(self, Answer, ButtonTypes): #button functions
        global ButtonPressed    #calls ButtonPressed
        if Answer == ButtonTypes:   #checks if correct answer has been selected
            ButtonPressed = True    #changes the button pressed variable
            global Correct  #calls Correct
            global i    #calls i 
            Correct = Correct + 1   #iterates Correct
            i = i + 1   #iterates i 
        elif Answer != ButtonTypes:     #checks if answer was incorrect
            i = i + 1   #iterates i
            ButtonPressed = True    #changes the button pressed variable
        self.root.destroy()     #destroys the window
        second = Question()     #Goes back to question class
        


    def Skip(self):     #skip button function
        global ButtonPressed    #calls ButtonPressed 
        ButtonPressed = True    #sets the button pressed to true
        global skips    #calls skips
        global i    #calls 9
        if skips < 3:   #checks if user is able to skip
            skips = skips + 1   #iterates skips
            i = i + 1   #iterates i
            self.root.destroy()     #destroys window
            second = Question()     #goes to Question class
        else:   #checks if user has gone over their skip limit
            ButtonPressed = False   #resets button pressed
            return  #returns to question function
     
class FinalScreen():    #Declares Results class
    def __init__(self):     #initialises window

        global Correct      #calls Correct
        percents = Correct/10   #calcultes percentage of correct answers
        #marking schedule and defines the grade
        if percents < 0.5:      
            Grade = "N/A"
        elif percents > 0.49 and percents < 0.7:
            Grade = "A"
        elif percents > 0.69 and percents < 0.9:
            Grade = "M"
        elif percents > 0.89 and percents < 1.01:
            Grade = "E"
        else:   #error handling
            quit()  #quits code
        self.root = tk.Tk()     #initialises window
        self.root.geometry('800x500')   #sets window size
        self.root.configure(bg='#cfe2f3')   #Sets background colour
        self.root.title("Percentages Math Quiz")    #sets window title 

        Title = tk.Label(self.root, text="Results", bg="#cceae3", font="Arial 18", width=15,
                         height=2, borderwidth=1, relief="solid").place(x=330, y=120)   #prints title
        Result = tk.Label(self.root, text=Grade + "\n" + "You Got: " + str(Correct) + "/10", bg="#cceae3", font="Arial 20",
                          width=20,
                          height=5, borderwidth=1, relief="solid").place(x=270, y=200)  #prints the results 

        TryAgn = tk.Button(self.root, text="TRY AGAIN", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                           width=12, height=1,
                           command=lambda: self.tryAgain()).place(x=640, y=450)     #initialises try again button

        QuitButton = tk.Button(self.root, text="QUIT", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                               width=12, height=1, command=lambda: quit()).place(x=10, y=450)   #initialises quit button

        self.root.mainloop()    #loops window

    def tryAgain(self):     #function for try again button
        self.root.destroy()     #destroys window
        StartScreen()   #goes to Questions class
        
app = StartScreen()     #sets starting window
