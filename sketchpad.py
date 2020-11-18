from tkinter import *
from line import Line
from circle import Circle

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
        self.parent = parent
        self.toolController = toolController
        
    def start_drawing(self, event):
        toolSelected = self.toolController.get_curr_tool()
        if toolSelected != None and not self.is_drawing:
            self.is_drawing = True
            if toolSelected == "Line":
                self.current_drawing = Line(self, event.x, event.y)
            elif toolSelected == "Circle":
                self.current_drawing = Circle(self, event.x, event.y)
        else:
            print("no tool is selected...")
    
    def draw(self, event):
        if self.is_drawing:
            self.current_drawing.delete()
            self.current_drawing.draw(event.x, event.y)

    def complete_drawing(self, event):
        if self.is_drawing:
            self.drawings[self.current_drawing.id] = self.current_drawing.get_props()
            self.is_drawing = False
        self.print_drawings()
    
    def print_drawings(self):
        for item in self.drawings.items():
            print(item)

    def draw_grid_overlay(self, grid_size):
        self.update_idletasks()
        print(self.winfo_height())
        window_height = self.winfo_height()
        window_width = self.winfo_width()
        
        for r in range(0,window_width,grid_size):
            self.create_line((r,0,r,window_height), width=0.5, fill="gray75")

        for r in range(0,window_height,grid_size):
            self.create_line((0,r,window_width,r), width=0.5, fill="gray75")

