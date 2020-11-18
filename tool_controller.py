class ToolController:
    def __init__(self):
        self.tools = {}
        self.curr_tool = None
    
    def add_tool(self, button_id, tool_name):
        if button_id not in self.tools:
            self.tools[button_id] = tool_name
            print("added " + tool_name)
    
    def get_curr_tool(self):
        if self.curr_tool:
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
