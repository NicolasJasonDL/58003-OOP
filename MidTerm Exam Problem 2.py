from tkinter import Tk, Label, Entry, Button, DISABLED, StringVar

def converter():
    meters = float(entryMeters.get())
    kilometers.set(str(meters/1000))


rootWindow = Tk()
rootWindow.title("Metric Units of Length")
rootWindow.geometry('500x200+0+0')
rootWindow.grid_columnconfigure(1, weight=1)

labelMiles = Label(rootWindow, text='Enter Distance in meters:')
labelMiles.grid(row=0, column=0)

labelKm = Label(rootWindow, text='Distance in kilometers:')
labelKm.grid(row=2, column=0)

entryMeters = Entry(rootWindow)
entryMeters.grid(row=0, column=1, sticky='w,e')

kilometers = StringVar()
entryKm = Entry(rootWindow, textvariable=kilometers, state=DISABLED)
entryKm.grid(row=2, column=1, sticky='w,e')

convertButton = Button(rootWindow, text='Convert', command=converter)
convertButton.grid(row=1, column=1)

rootWindow.mainloop()

