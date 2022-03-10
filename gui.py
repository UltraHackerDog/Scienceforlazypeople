from tkinter import *


def collectdata():
    Independent = Independentinfo.get()
    Dependent = dependentinfo.get()

window = Tk()
window.title("Science Solver")
window.configure(background="turquoise")
window.geometry("300x300")

Independentinfo = StringVar()
dependentinfo = StringVar()

heading = Label (text="ScienceSolver", bg="black", fg="white" , width="300")
heading.pack()

independentlabel = Label (window, text="What is your independent variable?", bg="turquoise", fg="black", font="Hubballi 10 bold")
independentlabel.pack()
independententry = Entry(textvariable=Independentinfo, width=20, bg="turquoise") 
independententry.pack()

dependentlabel = Label (window, text="What is your dependent variable?", bg="turquoise", fg="black", font="Hubballi 10 bold")
dependentlabel.pack()
dependententry = Entry(textvariable=dependentinfo, width=20, bg="turquoise") 
dependententry.pack()

Submit = Button(text="Submit", width="10", command=collectdata)
Submit.pack()




window.mainloop()
