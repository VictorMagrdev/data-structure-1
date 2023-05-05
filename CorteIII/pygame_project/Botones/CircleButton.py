import pygame
from .Button import Button

class CircleButton(Button):

    def __init__(self,coords):
        super().__init__(coords, 65, 65)
        self.value = 0

    def draw(self, screen):
        if self.selected:
            self.border = 0
        else:
            self.border = 3
        pygame.draw.rect(screen,(0,0,255), pygame.Rect(self.x , self.y, self.width, self.height), self.border)
        pygame.draw.circle(screen, (0, 0, 255),(((self.x+(self.x+self.width))/2),((self.y+(self.y+self.height))/2)), 25, 3)