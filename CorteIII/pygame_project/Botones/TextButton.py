import pygame
from .Button import Button

class TextButton(Button):

    def __init__(self, text, font_size, coords):
        super().__init__(coords, 0, 0)
        self.font = pygame.font.SysFont("Helvetica", font_size)
        self.text = text
        self.text_render = self.font.render(self.text,True,(250,250,250))
        self.width = self.text_render.get_width() + 20
        self.height = self.text_render.get_height() + 20

    def draw(self, screen, mouse_position):
        if self.is_mouse_contained(mouse_position):
            border_width = 0
        else:
            border_width = 3
        pygame.draw.rect(screen,(150,150,150), pygame.Rect(self.x, self.y, self.width, self.height), border_width)
        screen.blit(self.text_render,(self.x + 10, self.y + 10))



