from tkinter import *

class Sketchpad(Canvas):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, bg="white",)
        self.temp_line = None
        self.bind("<Button-1>", self.start_pos)
        self.bind("<B1-Motion>", self.display_temp_line)
        self.bind("<ButtonRelease-1>", self.add_line)
        
    def start_pos(self, event):
        print("called start_pos for canvas")
      # create a textbox to populate a length 
      #  textentry = Entry(self)
      #  self.create_window(event.x, event.y-25, window=textentry, height=20, width=40)
        self.lastx, self.lasty = event.x, event.y
    
    def display_temp_line(self, event):
        if self.temp_line != None:
            self.delete(self.temp_line)
            self.temp_line = None
        self.temp_line = self.create_line((self.lastx, self.lasty, event.x, event.y), width=3)

    def add_line(self, event):
        if self.temp_line != None:
            self.delete(self.temp_line)
        self.create_line((self.lastx, self.lasty, event.x, event.y), width=3)