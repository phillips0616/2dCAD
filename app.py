from tkinter import *
import tkinter.font as font
from tool_controller import ToolController
from sketchpad import Sketchpad
from file_cad import FileCAD
from PIL import Image, ImageTk


root = Tk()
root.geometry("800x800")

#build the basic file menu
def donothing():
    print("Hello,World")

def buildMenu():
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)

    filecad = FileCAD() # this needs to be called in a way that it can be passed the drawing properties...

    filemenu.add_command(label="open", command=donothing)
    filemenu.add_command(label="save", command=donothing)
    filemenu.add_command(label="save as...", command=donothing)

    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

toolController = ToolController()
def buildToolbar(self):
    font_size_15 = font.Font(size=11)
    #build frame for the toolbar that has the different drawing tools
    toolbar = Frame(root, bg="gray44", pady=2)
    #the toolbar will sit at the top and take up the width of the application
    toolbar.pack(side = TOP, fill="x")

    #add line button
    line_image = Image.open(r"images\line.png")
    line_image = line_image.resize((16,16), Image.ANTIALIAS)
    self.tk_image_line = ImageTk.PhotoImage(line_image)
    lineButton = Button(toolbar, text = "Line ", bg="gray64", fg="white", padx=4, pady=2, image = self.tk_image_line, compound = RIGHT)
    lineButton['font'] = font_size_15
    toolController.add_tool(lineButton, "Line")
    lineButton.configure(command = lambda: toolController.select_tool(lineButton))
    lineButton.pack(side = LEFT)

    #add circle button
    circle_image = Image.open(r"images\oval.png")
    circle_image = circle_image.resize((16,16), Image.ANTIALIAS)
    self.tk_image_circle = ImageTk.PhotoImage(circle_image)
    circleButton = Button(toolbar, text = "Circle ", bg="gray64", fg="white", padx=2, pady=2, image = self.tk_image_circle, compound = RIGHT)
    circleButton['font'] = font_size_15
    toolController.add_tool(circleButton, "Circle")
    circleButton.configure(command = lambda: toolController.select_tool(circleButton))
    circleButton.pack(side = LEFT)

buildMenu()
buildToolbar(root)


root.update_idletasks() 
sketchpad = Sketchpad(root, toolController)
sketchpad.pack(expand=True, fill='both')
sketchpad.draw_grid_overlay(18)

root.mainloop()