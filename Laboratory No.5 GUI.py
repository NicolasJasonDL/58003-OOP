#GUI Form

from tkinter import *
window = Tk()
window.title("Find the largest number")
window.geometry("400x300+20+10")

def findLargest():
    L = []
    L.append(eval(conOfent2.get()))
    L.append(eval(conOfent3.get()))
    L.append(eval(conOfent4.get()))
    conOfLargest.set(max(L))

lb11 = Label(window, text = "The program that Finds the Largest Number")
lb11.grid(row=0, column=1, columnspan=2, sticky=EW)
lb12 = Label(window,text="Enter first number: ")
lb12.grid(row=1, column=0, sticky=W)
conOfent2 = StringVar()
ent2 = Entry(window, bd=3, textvariable=conOfent2)
ent2.grid(row=1, column=1)
lb13 = Label(window, text="Enter second number: ")
lb13.grid(row=2, column=0)
conOfent3 = StringVar()
ent3 = Entry(window, bd=3, textvariable=conOfent3)
ent3.grid(row=2, column=1)
lb14 = Label(window, text="Entry third number: ")
lb14.grid(row=3, column=0, sticky=W)
conOfent4 = StringVar()
ent4 = Entry(window, bd=3, textvariable=conOfent4)
ent4.grid(row=3, column=1)

btn1 = Button(window,text = "Find the largest number", command=findLargest)
btn1.grid(row=4, column=1)
lb15 = Label(window, text="The largest number: ")
lb15.grid(row=5, column=0, sticky=W)
conOfLargest = StringVar()
ent5 = Entry(window, bd=3, state="readonly", textvariable=conOfLargest)
ent5.grid(row=5, column=1)

mainloop()