
import tkinter.filedialog as tkfile
import os

class FileSelector:
    def __init__(self):
        self.filelist = []
        self.index = -1

    def selectFolder(self, path=None):
        if path is None:
            folder = tkfile.askdirectory()
        else:
            folder = path

        os.chdir(folder)
        for pdfdoc in os.listdir(folder):
            self.filelist.append(pdfdoc)

# ---- end ----
