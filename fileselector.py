
import tkinter.filedialog as tkfile
import os

class FileSelector:
    def __init__(self):
        self.filelist = []
        self.file_dictionary = {}
        self.index = -1

    def selectFolder(self, path=None):
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

    def selectFolder2(self, spath):
        filelist = tkfile.askopenfilenames(
                title = "Select PDF file(s)",
                initialdir = spath,
                filetypes = (("PDF", "*.pdf"), ("All", "*.*"))
                )
        #
        # check for 'cancel' on dialog
        #
        if not filelist:
            return False
        for f in filelist:
            self.file_dictionary[os.path.basename(f)] = f
        return True

    def clearList(self):
        self.file_dictionary.clear()

    def getList(self):
        return self.file_dictionary

    def removeKey(self, item):
        del self.file_dictionary[item]


# ---- end ----
