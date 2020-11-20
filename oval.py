class Oval:
    def __init__(self, canvas, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = None
        self.end_y = None
        self.canvas = canvas
        self.id = None

    
    def draw(self, new_x, new_y):
        self.id = self.canvas.create_oval((self.start_x, self.start_y, new_x, new_y), width=3)
        self.end_x, self.end_y = new_x, new_y

    def delete(self):
        self.canvas.delete(self.id)
    
    def get_props(self):
        return ["Circle", self.start_x, self.start_y, self.end_x, self.end_y]