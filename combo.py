import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title("Combobox")
window.geometry("500x250")

def choice(event):
    month = event.widget.get()
    print("Your birth month:", month)

ttk.Label(window, text="Choose your birth month", background='light yellow', foreground='black', font=("Times New Roman", 15)).grid(row=0, column=1)

n = tk.StringVar()
month = ttk.Combobox(window, width=27, textvariable=n)
month['values'] = ("January", "February", 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
month.grid(column=1, row=5)
month.bind("<<ComboboxSelected>>", choice)

window.mainloop()
