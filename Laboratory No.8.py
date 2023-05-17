from tkinter import *


class ListBoxTest:
    def __init__(self):
        self.root = Tk()
        self.root.title("List Box")
        self.label = Label(self.root, text="Insert an item:")
        self.label.pack(pady=10)
        self.insert_entry = Entry(self.root)
        self.insert_entry.pack(padx=10)
        self.insert_button = Button(self.root, text="Insert", command=self.InsertSelection)
        self.insert_button.pack(pady=5)
        self.delete_button = Button(self.root, text="Delete", command=self.DeleteSelection)
        self.delete_button.pack(pady=5)
        self.list_box_1 = Listbox(self.root, selectmode=EXTENDED)
        self.list_box_1.pack(padx=10, pady=10, fill=BOTH, expand=True)

        self.list_box_1.insert(END, "C++")
        self.list_box_1.insert(END, "Python")
        self.list_box_1.insert(END, "HTML")
        self.list_box_1.insert(END, "Java")
        self.root.mainloop()

    def InsertSelection(self):
        item = self.insert_entry.get()
        if item:
            self.list_box_1.insert(END, item)
            self.insert_entry.delete(0, END)

    def DeleteSelection(self):
        items = self.list_box_1.curselection()
        pos = 0
        for i in items:
            idx = int(i) - pos
            self.list_box_1.delete(idx, idx)
            pos += 1

lbt = ListBoxTest()