
class Button:

    def __init__(self, coords, width, height):
        self.selected = False
        self.x = coords[0]
        self.y = coords[1]

        self.width = width
        self.height = height

    def is_mouse_contained(self, mouse_position):
        return (mouse_position[0] > self.x and 
                mouse_position[1] > self.y and 
                mouse_position[0] < self.x + self.width and 
                mouse_position[1] < self.y + self.height)

    def toggle_selected(self):
        if not self.selected:
            self.selected = True
        else:
            self.selected = False
    
    def set_selected_false(self):
        self.selected = False