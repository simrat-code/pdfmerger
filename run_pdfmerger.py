#!/usr/bin/env python3

import tkinter as tk

from fileselector import FileSelector

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.fs = FileSelector()
        #
        # calling initialise functions
        #
        self._createWidgets()
        self._bindEvents()
        self._setLayout()

    def _createWidgets(self):
        self.grid(row=6, column=5, sticky="nsew")
        self.master.minsize(300, 300)
        self.browse = tk.Button(self, text="Browse")
        self.process = tk.Button(self, text="Process")
        self.lbox = tk.Listbox(self)
        self.label2 = tk.Label(self, text="File Name")
        self.entry = tk.Entry(self) 

    def _bindEvents(self):
        self.browse.bind('<ButtonRelease-1>', self._fillListBox)

    def _setLayout(self):
        self.label2.grid(row=0, column=0, 
                        sticky='e', 
                        padx=2, pady=2)
        self.entry.grid(row=0, column=1, 
                        columnspan=2, 
                        padx=2, pady=2)
        self.lbox.grid(row=1, column=0, 
                        rowspan=5, columnspan=4,
                        sticky='nsew', 
                        padx=2, pady=0)
        self.browse.grid(row=1, column=4)
        self.process.grid(row=2, column=4)

    def _fillListBox(self, event=None):
        if self.fs.selectFolder():
            #
            # folder parsing is success
            # need to populate list-box
            #
            self.lbox.delete(0, 'end')
            for item in self.fs.getList():
                self.lbox.insert('end', item)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


