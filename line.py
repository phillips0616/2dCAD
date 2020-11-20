class Line:
    def __init__(self, canvas, start_x, start_y, max_x, max_y):
        self.start_x, self.start_y = min(start_x, max_x), min(start_y, max_y)
        self.max_x = max_x
        self.max_y = max_y
        self.end_x = None
        self.end_y = None
        self.canvas = canvas
        self.id = None

    
    def draw(self, new_x, new_y):
        self.id = self.canvas.create_line((self.start_x, self.start_y, min(new_x, self.max_x), min(self.max_y,new_y)), width=3)
        self.end_x, self.end_y = new_x, new_y

    def delete(self):
        self.canvas.delete(self.id)
    
    def get_props(self):
        return ["Line", self.start_x, self.start_y, self.end_x, self.end_y]