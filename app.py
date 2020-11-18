from tkinter import *
from tool_controller import ToolController
from sketchpad import Sketchpad


root = Tk()
root.geometry("640x600")

#build the basic file menu
def donothing():
    print("Hello,World")

def buildMenu():
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)

    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_command(label="Save as...", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)

    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

toolController = ToolController()
def buildToolbar():

    #build frame for the toolbar that has the different drawing tools
    toolbar = Frame(root, bg="gray44")
    #the toolbar will sit at the top and take up the width of the application
    toolbar.pack(side = TOP, fill="x")

    #add line button
    lineButton = Button(toolbar, text = "Line", bg="gray64", fg="white", padx=2, pady=2)
    toolController.add_tool(lineButton, "Line")
    lineButton.configure(command = lambda: toolController.select_tool(lineButton))
    lineButton.pack(side = LEFT)

    #add circle button
    circleButton = Button(toolbar, text = "Circle", bg="gray64", fg="white", padx=2, pady=2)
    toolController.add_tool(circleButton, "Circle")
    circleButton.configure(command = lambda: toolController.select_tool(circleButton))
    circleButton.pack(side = LEFT)

buildMenu()
buildToolbar()


root.update_idletasks() 
sketchpad = Sketchpad(root, toolController)
sketchpad.pack(expand=True, fill='both')
sketchpad.draw_grid_overlay(18)

root.mainloop()