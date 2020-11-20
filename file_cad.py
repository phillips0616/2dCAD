from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
class FileCAD:
    def __init__(self, sketchpad):
        self.sketchpad = sketchpad
        self.open_files_path = None
        self.is_saved = True

    def open_file(self):
        file = askopenfile(mode='r', filetypes=[('2dCAD Drawings', '*.cad')])

    def save(self):
        pass

    def save_as(self):
        files = [('2dCAD Drawings', '*.cad')]
        file = asksaveasfile(filetypes = files, defaultextension = files)

        file.write("window_height:" + str(self.sketchpad.max_y) + "\n")
        file.write("window_width:" + str(self.sketchpad.max_x) + "\n")
        for value in self.sketchpad.drawings.values():
            for item in value:
                file.write(str(item) + ",")
            file.write("\n")
            
            