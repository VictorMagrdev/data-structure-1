import pygame 
import sys
from animal import Animal 

class AnimalsPirata:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((800,500))
        pygame.display.set_caption("Animals Pirata")
        self.color=(230,230,230)
        self.animal =Animal(self) 

    def corre_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type  == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.color)
            #mostrar imagen
            self.animal.corre()
            pygame.display.flip()

if __name__=="__main__":
    a=AnimalsPirata() 
    a.corre_juego()