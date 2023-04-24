from tkinter import *

win = Tk()
win.geometry("490x300+10+10")
win.title("Grid Manager")

text1 = Entry(bd=2)
text1.grid(row=0, column=0, sticky=N)
text1.insert(0, "row 0, column 0")

text2 = Entry(bd=2)
text2.grid(row=0, column=1, sticky=E)
text2.insert(0, "row 0, column 1")

text3 = Entry(bd=2)
text3.grid(row=0, column=2, sticky=N)
text3.insert(0, "row 0, column 2")

text4 = Entry(bd=2)
text4.grid(row=1, column=0, sticky=N)
text4.insert(1, "row 1, column 0")

text5 = Entry(bd=2)
text5.grid(row=1, column=1, sticky=N)
text5.insert(1, "row 1, column 1")

text6 = Entry(bd=2)
text6.grid(row=1, column=2, sticky=N)
text6.insert(1, "row 1, column 2")

text7 = Entry(bd=2)
text7.grid(row=2, column=0, sticky=N)
text7.insert(2, "row 3, column 0")

text8 = Entry(bd=2)
text8.grid(row=2, column=1, sticky=N)
text8.insert(2, "row 2, column 1")

text9 = Entry(bd=2)
text9.grid(row=2, column=2, sticky=N)
text9.insert(2, "row 2, column 2")

win.mainloop()