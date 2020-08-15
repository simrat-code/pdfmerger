
import tkinter.filedialog as tkfile
import os

class FileSelector:
    def __init__(self):
        self.filelist = []
        self.index = -1

    def selectFolder(self, event=None, path=None):
        self.clearList()
        if path is None:
            folder = tkfile.askdirectory()
            #
            # check for 'cancel' on dialog
            #
            if not folder:
                return False
        else:
            folder = path
        os.chdir(folder)
        for pdfdoc in os.listdir(folder):
            if pdfdoc.lower().endswith("pdf"):
                self.filelist.append(pdfdoc)
        return True

    def selectFolder2(self, event=None, path=None):
        self.clearList()
        if path is None:
            ifolder = tkfile.askopenfilenames(
                    filetypes=(("PDF", "*.pdf"), ("All", "*.*"))
                    )
            #
            # check for 'cancel' on dialog
            #
            if not folder:
                return False
        else:
            folder = path
        os.chdir(folder)
        for pdfdoc in os.listdir(folder):
            if pdfdoc.lower().endswith("pdf"):
                self.filelist.append(pdfdoc)
        return True

    def clearList(self):
        self.filelist.clear()

    def getList(self):
        return self.filelist

# ---- end ----
