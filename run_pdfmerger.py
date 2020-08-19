#!/usr/bin/env python3

import tkinter as tk
import os

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
        self.grid(row=7, column=5, sticky="nsew")
        self.master.minsize(300, 300)
        self.label2 = tk.Label(self, text="File Name")
        self.entry = tk.Entry(self) 
        self.browse = tk.Button(self, text="Browse")
        self.process = tk.Button(self, text="Process")
        self.lbox = tk.Listbox(self, selectmode=tk.SINGLE) #tk.EXTENDED)
        self.moveup = tk.Button(self, text="Up")
        self.movedown = tk.Button(self, text="Down")

    def _bindEvents(self):
        self.browse.bind('<ButtonRelease-1>', self._fillListBox)
        self.moveup.bind('<ButtonRelease-1>', self._moveup)
        self.movedown.bind('<ButtonRelease-1>', self._movedown)

    def _setLayout(self):
        self.label2.grid(row=0, column=0, 
                        sticky='e', 
                        padx=2, pady=2)
        self.entry.grid(row=0, column=1, 
                        columnspan=2, 
                        padx=2, pady=2)
        self.browse.grid(row=1, column=4)
        self.process.grid(row=2, column=4)
        self.lbox.grid(row=1, column=0, 
                        rowspan=5, columnspan=4,
                        sticky='nsew', 
                        padx=2, pady=0)
        self.moveup.grid(row=6, column=2)
        self.movedown.grid(row=6, column=3)

    def _fillListBox(self, event=None):
        if self.fs.selectFolder2(spath = os.environ['HOME']):
            #
            # folder parsing is success
            # need to populate list-box
            #
            self.lbox.delete(0, 'end')
            for item in self.fs.getList().keys():
                self.lbox.insert('end', item)

    def _moveup(self, event=None):
        index = self.lbox.curselection()
        if not index:
            return
        #
        # list of selected items returned
        # in case of tk.EXTENDED
        #
        for pos in index:
            if pos == 0:
                continue
            text = self.lbox.get(pos)
            self.lbox.delete(pos)
            self.lbox.insert(pos - 1, text)
            #
            # to keep the selection
            #
            self.lbox.selection_set(pos - 1)

    def _movedown(self, event=None):
        index = self.lbox.curselection()
        if not index:
            return
        for pos in index:
            if pos == self.lbox.size() - 1:
                # 
                # checking if current selection is last item
                #
                continue
            text = self.lbox.get(pos)
            self.lbox.delete(pos)
            self.lbox.insert(pos + 1, text)
            self.lbox.selection_set(pos + 1)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


