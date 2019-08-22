from tkinter import *
# from CalcFunctions import *
# from BasicFunctions import *
# from StatFunctions import *

class MathSoftware(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.initUI()

    def initUI(self):

        self.master.title("Math 4 U 0.1")

        menubar = Menu(self.master)
        self.master.config(menu = menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label = "Exit", command = self.onExit)
        menubar.add_cascade(label = "File", menu=fileMenu)

        # tab for basic functions

        basicMenu = Menu(menubar)

        basicMenu.add_command(label="Compare Numbers")
        basicMenu.add_command(label="Factorize")
        basicMenu.add_command(label= "GCF")
        basicMenu.add_command(label="LCM")
        basicMenu.add_command(label="10th Power")
        basicMenu.add_command(label="Absolute Value")
        basicMenu.add_command(label="Expand Function")

        menubar.add_cascade(label= "Basic", menu = basicMenu)

        # tab for calculus functions

        calcMenu = Menu(menubar)

        calcMenu.add_command(label="Derivative")
        calcMenu.add_command(label="Definite Integral")
        calcMenu.add_command(label="Indefinite Integral")
        calcMenu.add_command(label="Find Limit")
        calcMenu.add_command(label="Expand Series")

        menubar.add_cascade(label="Calculus", menu=calcMenu)

        # tab for statistics functions

        statMenu = Menu(menubar)

        statMenu.add_command(label="Mean")
        statMenu.add_command(label="Median")
        statMenu.add_command(label="Mode")
        statMenu.add_command(label="Sum of the Set")
        statMenu.add_command(label="Factorial")
        statMenu.add_command(label="Product of the Set")
        statMenu.add_command(label="Max of the Set")
        statMenu.add_command(label="Min of the Set")
        statMenu.add_command(label="Variance of the Set")

        menubar.add_cascade(label="Statistics", menu=statMenu)



    def onExit(self):
        self.quit()

    


def main():
    root = Tk()
    root.option_add('*tearOff', FALSE)
    root.geometry("400x400")
    app = MathSoftware(root)
    root.mainloop()

main()



