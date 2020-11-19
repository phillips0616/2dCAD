from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
class FileCAD:
    def __init__(self):
        self.open_files_path = None
        self.is_saved = True

    def open_file(self):
        file = askopenfile(mode='r', filetypes=[('2dCAD Drawings', '*.cad')])

    def save(self, drawing_properties):
        # f = open("test.cad", "w")
        # f.write("this is a test")
        # f.close()
        pass

    def save_as(self, drawing_properties):
        files = [('2dCAD Drawings', '*.cad')]
        file = asksaveasfile(filetypes = files, defaultextension = files)