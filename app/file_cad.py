from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile

class FileCAD:
    def __init__(self, sketchpad):
        self.sketchpad = sketchpad
        self.open_files_path = None
        self.is_saved = True

    def open_file(self):
        file = askopenfile(mode='r', filetypes=[('2dCAD Drawings', '*.cad')])

        self.sketchpad.clear_sketchpad()

        #we aren't going to do anything with these two lines until we worry about window resizing
        window_height = file.readline()
        window_width = file.readline()

        for line in file:
            items = line.split(",")
            tool = items[0]
            start_x = int(items[1])
            start_y = int(items[2])
            end_x = int(items[3])
            end_y = int(items[4])

            self.sketchpad.load_drawing(tool,start_x,start_y,end_x,end_y)

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
    
    def clear(self):
        self.sketchpad.clear_sketchpad()