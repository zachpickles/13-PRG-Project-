import tkinter as tk

class StartScreen():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.configure(bg='#cfe2f3')
        self.root.title("Percentages Math Quiz")
        Title = tk.Label(self.root, text="PERCENTAGES MATH QUIZ", bg="#cceae3", font="Arial 18",width=28,height=3 ,borderwidth=1, relief="solid").place(x=225, y=80)
        Quit = tk.Button(self.root,
                           text = 'QUIT', borderwidth=1, relief="solid", bg="#cceae3", width=15, height=2, font="Arial 14",
                           command = self.quit).place(x=610, y=425)
        Start = tk.Button(self.root,
                            text = "START", borderwidth=1, relief="solid", bg="#cceae3", width=20, height=3, font="Arial 14",
                            ).place(x=320, y=200)
        InstTitle = tk.Label()
        Inst = tk.Label()
        self.root.mainloop()

    def quit(self):
        self.root.destroy()




app = StartScreen()
