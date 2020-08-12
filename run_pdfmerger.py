#!/usr/bin/env python3

import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.master.minsize(300, 300)
        self.lbox = tk.Listbox(self.master)
        self.lbox.insert(1, "First")
        self.lbox.insert(2, "Second")

        self.lbox.pack(fill='both')



if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


