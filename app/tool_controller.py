from tkinter import *
import tkinter.font as font
from PIL import Image, ImageTk

class ToolController:
    def __init__(self, toolbar):
        self.tools = {}
        self.curr_tool = None
        self.toolbar = toolbar
        self.button_images = {}
    
    def add_tool(self, button_id, tool_name):
        if button_id not in self.tools:
            self.tools[button_id] = tool_name
            print("added " + tool_name + " tool")
    
    def get_curr_tool(self):
        if self.curr_tool:
            print("The currently selected tool is " + self.curr_tool[1])
            return self.curr_tool[1]
        
        return None

    def select_tool(self, button_id):
        if self.curr_tool != None and self.curr_tool[1] != self.tools[button_id]:
            
            self.curr_tool[0]['bg'] = "gray64"
            self.curr_tool[0]['fg'] = "white"
            
            self.curr_tool = (button_id, self.tools[button_id])
            button_id['bg'] = "white"
            button_id['fg'] = "black"
        elif self.curr_tool == None:
            self.curr_tool = (button_id, self.tools[button_id])
            button_id['bg'] = "white"
            button_id['fg'] = "black"

        print("You have selected " + self.curr_tool[1] + " tool")
    
    def create_tool(self, image_path, tool_name):
        font_size_15 = font.Font(size=11)
        image = Image.open(r'' + image_path)
        image = image.resize((16,16), Image.ANTIALIAS)
        tk_image = ImageTk.PhotoImage(image)
        button = Button(self.toolbar, text = tool_name + " ", bg="gray64", fg="white", padx=4, pady=2, compound = RIGHT)
        self.button_images[button] = tk_image #need to store each image for each button so that it doesn't get garbage collected
        button ['image'] = self.button_images[button]
        button['font'] = font_size_15
        self.add_tool(button, tool_name)
        button.configure(command = lambda: self.select_tool(button))
        button.pack(side = LEFT)

