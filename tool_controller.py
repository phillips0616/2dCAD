class ToolController:
    def __init__(self):
        self.tools = {}
        self.curr_tool = None
    
    def add_tool(self, button_id, tool_name):
        if button_id not in self.tools:
            self.tools[button_id] = tool_name
            print("added " + tool_name)
    
    def get_curr_tool(self):
        return self.curr_tool

    def select_tool(self, button_id):
        print(button_id)
        self.curr_tool = self.tools[button_id]
        print(self.curr_tool)
        #do something to let canvas know a new tool has been selected
        print("You have selected " + self.curr_tool + " tool")
