from tkinter import *
import tkinter.font as font
from tool_controller import ToolController
from sketchpad import Sketchpad
from file_cad import FileCAD

class App:
    def __init__(self, root):
        self.root = root
        self.toolbar = self.build_toolbar_view()
        self.toolbar_controller = ToolController(self.toolbar)
        self.sketchpad = Sketchpad(self.root, self.toolbar_controller)
        self.fileCAD = FileCAD(self.sketchpad)
        self.build_filmenu_view()
        self.build_sketchpad()
    
    def set_geometry(self):
        self.root.geometry("800x800")
    
    def build_filmenu_view(self):
        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0) #I've made a change

        filemenu.add_command(label="open", command=self.fileCAD.open_file)
        filemenu.add_command(label="save", command=self.fileCAD.save)
        filemenu.add_command(label="save as...", command=self.fileCAD.save_as)
        filemenu.add_command(label="clear sketchpad", command=self.fileCAD.clear)

        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)
    
    def build_toolbar_view(self):
        toolbar = Frame(self.root, bg="gray44", pady=2)
        toolbar.pack(side = TOP, fill="x")
        return toolbar
    
    def add_tool_to_toolbar(self, image_path,tool_name):
        self.toolbar_controller.create_tool(image_path, tool_name)

    def build_sketchpad(self):
        self.sketchpad.pack(expand=True, fill='both')
        self.sketchpad.draw_grid_overlay(18)

root = Tk()
root.geometry("800x800")
root.update_idletasks() 

app = App(root)
app.add_tool_to_toolbar(r"app\images\oval.png", "Oval")
app.add_tool_to_toolbar(r"app\images\line.png", "Line")

root.mainloop()