import pygame

class Animal:
    def __init__(self,a_game):
        self.screen= a_game.screen
        self.screen_rect=a_game.screen.get_rect()
        #zorro
        self.zorro=pygame.image.load("zorro.jpg")
        self.zorro = pygame.transform.scale(self.zorro,(100,100)) 
        #alce

        self.alce=pygame.image.load("alce.jpg")
        self.alce = pygame.transform.scale(self.alce,(50,50))
        
        

    def corre(self):
        #dibujar imagen 
        self.screen.blit(self.zorro,(50,87))#primer numero en la posicion linea recta #segundo numero arriba que tan alto esta
        self.screen.blit(self.alce,(170,87))#primero lo corre en linea recta segundo si arriba o abajo 