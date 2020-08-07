import tkinter as tk
global i
i = 0
Questions = "stuff"
ButtonsText = ["a", "b", "c"]
class Questions ():
    #def __init__ (self):
        #self.root = tk.Tk()
        #self.root.geometry('800x500')
        #self.root.configure(bg='#cfe2f3')
        #self.root.title("Percentages Math Quiz")

        #Multiple Choice Questions
        #QuestNum = tk.Label(self.root, text="Question "+str(i)+"/10", bg="#cceae3", font="Arial 14",width=15,height=2 ,borderwidth=1, relief="solid").place(x=5, y=5)
        #Quest = tk.Label(self.root, text=Questions, bg="#cceae3", font="Arial 18",width=28,height=3 ,borderwidth=1, relief="solid").place(x=210, y=150)

        #ButtonA = tk.Button(self.root,
                            #text=str(ButtonsText[0]), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid", width=6, height=1,
                            #command = lambda : self.test()).place(x=260, y=260)

        #ButtonB = tk.Button(self.root,
                            #text=str(ButtonsText[1]), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            #width=6, height=1,
                            #command=lambda: self.test()).place(x=360, y=260)

        #ButtonC = tk.Button(self.root,
                            #text=str(ButtonsText[2]), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            #width=6, height=1,
                            #command=lambda: self.test()).place(x=460, y=260)
        #SkipButton = tk.Button(self.root,
                               #text="Skip Question", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                               #width=12, height=1,
                               #command=lambda : self.test()).place(x=640, y=450)

    #True False Questions
    def __init__ (self):
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.configure(bg='#cfe2f3')
        self.root.title("Percentages Math Quiz")

        QuestNum = tk.Label(self.root, text="Question " + str(i) + "/10", bg="#cceae3", font="Arial 14", width=15,
                            height=2, borderwidth=1, relief="solid").place(x=5, y=5)
        Quest = tk.Label(self.root, text=Questions, bg="#cceae3", font="Arial 18", width=28, height=3, borderwidth=1,
                         relief="solid").place(x=210, y=150)

        ButtonA = tk.Button(self.root,
                            text=str(ButtonsText[0]), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.test()).place(x=320, y=260)

        ButtonB = tk.Button(self.root,
                            text=str(ButtonsText[1]), bg="#cceae3", font="Arial 18", borderwidth=1, relief="solid",
                            width=6, height=1,
                            command=lambda: self.test()).place(x=420, y=260)

        SkipButton = tk.Button(self.root,
                               text="Skip Question", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                               width=12, height=1,
                               command=lambda: self.test()).place(x=640, y=450)


        self.root.mainloop()



    def test(self):
        global i
        i = i + 1



app = Questions()