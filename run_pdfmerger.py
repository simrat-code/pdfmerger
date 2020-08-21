#!/usr/bin/env python3

import tkinter as tk
import subprocess
import os
import sys

from tkinter import messagebox
from fileselector import FileSelector

class Application(tk.Frame):
    def __init__(self, master=None, root_path=None):
        super().__init__(master)
        self.master = master
        self.root_path = root_path
        self.fs = FileSelector()
        self.outfile = tk.StringVar()
        #
        # calling initialise functions
        #
        self.master.resizable(width=False, height=False)
        self._createWidgets()
        self._bindEvents()
        self._setLayout()

    def _createWidgets(self):
        self.grid(row=7, column=5, sticky="nsew")
        #self.master.minsize(325, 245)
        self.label2 = tk.Label(self, text="File Name")
        self.entry = tk.Entry(self, textvariable=self.outfile) 
        self.browse = tk.Button(self, text="Browse")
        self.process = tk.Button(self, text="Process")
        self.lbox = tk.Listbox(self, selectmode=tk.SINGLE) #tk.EXTENDED)
        self.labelA = tk.Label(self, text="")
        self.labelB = tk.Label(self, text="")
        self.moveup = tk.Button(self, text=" Up ")
        self.movedown = tk.Button(self, text="Down")

    def _bindEvents(self):
        self.browse.bind('<ButtonRelease-1>', self._fillListBox)
        self.moveup.bind('<ButtonRelease-1>', self._moveup)
        self.movedown.bind('<ButtonRelease-1>', self._movedown)
        self.process.bind('<ButtonRelease-1>', self._process)

    def _setLayout(self):
        self.label2.grid(
                row=0, column=0, sticky='ew', 
                padx=2, pady=2
                )
        self.entry.grid(
                row=0, column=1, sticky="ew",
                columnspan=3, 
                padx=2, pady=2
                )
        self.browse.grid(
                row=1, column=4, sticky="ew"
                )
        self.process.grid(
                row=2, column=4, sticky="ew"
                )
        self.lbox.grid(
                row=1, column=0, sticky="nsew",
                rowspan=5, columnspan=4,
                padx=2, pady=0
                )
        self.labelA.grid(
                row=6, column=0, sticky="ew"
                )
        self.labelB.grid(
                row=6, column=1, sticky="ew"
                )
        self.moveup.grid(
                row=6, column=2, sticky="ew",
                padx=0, pady=2
                )
        self.movedown.grid(
                row=6, column=3, sticky="ew",
                padx=2, pady=2
                )

    def _fillListBox(self, event=None):
        if self.fs.selectFolder2(spath = self.root_path):
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

    def _process(self, event=None):
        try:
            self._workerProcess()
        except:
            #
            # to catch any missed exception
            #
            print(sys.exc_info()[0])
            messagebox.showerror(
                    'Failed',
                    'Unable to process due to exception\n' \
                    'try run in terminal'
                    )

    def _workerProcess(self):
        if not self._validate():
            return
        cmd = [
                'gs', 
                '-dBATCH', '-dNOPAUSE', 
                '-sDEVICE=pdfwrite',
                '-dPDFSETTINGS=/prepress'
                #'-sOutputFile=##OUTNAME##'
                ]
        #
        # check out-filename
        # and append to final 'gs' command
        #
        outfile = '-sOutputFile='+ self.root_path +'/'+ self.outfile.get()
        if not outfile.endswith('.pdf'):
            outfile = outfile + '.pdf'
        cmd.append(outfile)
        #
        # append PDF files to final commmand
        #
        var_dictionary = self.fs.getList()
        for item in self.lbox.get(0, 'end'):
            cmd.append(var_dictionary[item])
        #
        # execute final command
        #
        print(cmd)
        proc = subprocess.Popen(cmd,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE)
        stdout, stderr = proc.communicate()
        if stderr:
            messagebox.showerror(
                    'Failed',
                    stderr
                    )
        else:
            messagebox.showinfo(
                    'Completed',
                    'Operation Success'
                    )

    def _validate(self):
        if not self.fs.getList():
            messagebox.showerror(
                    'Missing input',
                    'Kindly select input pdf file(s)'
                    )
            return False
        if not self.outfile.get():
            messagebox.showerror(
                    'Missing entry',
                    'Kindly provide Filename'
                    )
            return False
        return True


if __name__ == "__main__":
    root = tk.Tk()
    rpath = os.environ['HOME']
    app = Application(master=root, root_path=rpath)
    app.mainloop()


