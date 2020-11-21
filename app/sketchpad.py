from tkinter import *
from line import Line
from oval import Oval
import math

class Sketchpad(Canvas):
    def __init__(self, parent, toolController, **kwargs):
        super().__init__(parent, bg="white",)
        self.temp_line = None
        self.is_drawing = False
        self.current_drawing = None
        self.bind("<Button-1>", self.start_drawing)
        self.bind("<B1-Motion>", self.draw)
        self.bind("<ButtonRelease-1>", self.complete_drawing)
        self.drawings = {}
        self.max_x = None
        self.max_y = None
        self.length_label = None
        self.parent = parent
        self.toolController = toolController
        
    def start_drawing(self, event):
        toolSelected = self.toolController.get_curr_tool()
        if toolSelected != None and not self.is_drawing:
            self.is_drawing = True
            self.length_label = Label(self)
            self.length_label.pack(side=TOP, anchor=NE)
            if toolSelected == "Line":
                self.current_drawing = Line(self, event.x, event.y, self.max_x, self.max_y)
            elif toolSelected == "Oval":
                self.current_drawing = Oval(self, event.x, event.y, self.max_x, self.max_y)
        else:
            print("no tool is selected...")
    
    def draw(self, event):
        if self.is_drawing:
            self.current_drawing.delete()
            self.length_label['text'] = str(round(self.current_drawing.calculate_length(event.x, event.y),2)) + " in" #im sorry im American...
            self.current_drawing.draw(event.x, event.y)

    def complete_drawing(self, event):
        if self.is_drawing:
            self.drawings[self.current_drawing.id] = self.current_drawing.get_props()
            self.is_drawing = False
            self.length_label.destroy()
        self.print_drawings()
    
    def print_drawings(self):
        for value in self.drawings.values():
            print(value)
    
    def get_drawings(self):
        return self.drawings

    def draw_grid_overlay(self, grid_size):
        self.update_idletasks()
        print(self.winfo_height())
        #this is a bad place to do this... fix this
        self.max_y = self.winfo_height()
        self.max_x = self.winfo_width()
        
        for r in range(0,self.max_x,grid_size):
            self.create_line((r,0,r,self.max_y), width=0.5, fill="gray85")

        for r in range(0,self.max_y,grid_size):
            self.create_line((0,r,self.max_x,r), width=0.5, fill="gray85")
    
    def clear_sketchpad(self):
        for drawing in self.drawings.keys():
            self.delete(drawing)

        self.drawings.clear()

    def load_drawing(self, tool, start_x, start_y, end_x, end_y):
        toolSelected = tool
        if toolSelected != None:
            if toolSelected == "Line":
                self.current_drawing = Line(self, start_x, start_y, self.max_x, self.max_y)
            elif toolSelected == "Oval":
                self.current_drawing = Oval(self, start_x, start_y, self.max_x, self.max_y)
            self.current_drawing.draw(end_x, end_y)
            self.drawings[self.current_drawing.id] = self.current_drawing.get_props()
        else:
            print("no tool is selected...")