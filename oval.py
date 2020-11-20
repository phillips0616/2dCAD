class Oval:
    def __init__(self, canvas, start_x, start_y, max_x, max_y):
        self.start_x = start_x
        self.start_y = start_y
        self.max_x = max_x
        self.max_y = max_y
        self.end_x = None
        self.end_y = None
        self.canvas = canvas
        self.id = None

    
    def draw(self, new_x, new_y):
        #this safety check doesn't work perfectly for oval shapes. Part of the arc of the oval can still be off screen.
        safe_x = min(new_x, self.max_x) if min(new_x, self.max_x) > 0 else 0
        safe_y = min(new_y, self.max_y) if min(new_y, self.max_y) > 0 else 0
        self.id = self.canvas.create_oval((self.start_x, self.start_y, safe_x, safe_y), width=3)
        self.end_x, self.end_y = safe_x, safe_y

    def delete(self):
        self.canvas.delete(self.id)
    
    def get_props(self):
        return ["Circle", self.start_x, self.start_y, self.end_x, self.end_y]