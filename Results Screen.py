import tkinter as tk
GRD = "E"
Corct = 10
class ResScreen():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x500')
        self.root.configure(bg='#cfe2f3')
        self.root.title("Percentages Math Quiz")

        Title = tk.Label(self.root, text="Results", bg="#cceae3", font="Arial 18", width=15,
                            height=2, borderwidth=1, relief="solid").place(x=330, y=120)
        Result = tk.Label(self.root, text=GRD + "\n" + "You Got: " + str(Corct) + "/10", bg="#cceae3", font="Arial 20", width=20,
                            height=5, borderwidth=1, relief="solid").place(x=270, y=200)

        TryAgn = tk.Button(self.root, text="TRY AGAIN", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",
                               width=12, height=1,
                               command=lambda: self.Test()).place(x=640, y=450)

        SkipButton = tk.Button(self.root,text="QUIT", bg="#cceae3", font="Arial 16", borderwidth=1, relief="solid",width=12, height=1,command=lambda:self.Test()).place(x=10, y=450)


        self.root.mainloop()
    def Test(self):
        print("Test")

app = ResScreen()