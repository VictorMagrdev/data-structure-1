import pygame
from .Button import Button

class TriangleButton(Button):

    def __init__(self,coords):
        super().__init__(coords, 65, 65)
        self.value = 2

    def draw(self, screen):
        if self.selected:
            self.border = 0
        else:
            self.border = 3
        pygame.draw.rect(screen,(255,0,0), pygame.Rect(self.x , self.y, self.width, self.height), self.border)
        pygame.draw.polygon(screen, (255, 0, 0), ((self.x+10,self.y+self.height-10),(self.x+10+((self.width-20)/2),self.y+10),(self.x-10+self.width,self.y+self.height-10)),3)