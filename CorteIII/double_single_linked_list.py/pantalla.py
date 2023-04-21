import pygame,sys
pygame.init()

class Animal:
    def __init__(self,a_game):
        self.screen= a_game.screen
        self.screen_rect=a_game.screen.get_rect()
        self.image=pygame.image.load("zorro.jpg")       
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom



#definir colores
NEGRO =(0, 0, 0)
BLANCO=(255,255,255)
VERDE=(0,255,0)
ROJO=(255,0,0)
AZUL=(0,0,255)








size=(800,500)

#crear ventana 
screen=pygame.display.set_mode(size)


while True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            sys.exit()
# colores de fondo 
    screen.fill(BLANCO)

#zona de dibujo 
    pygame.draw.line(screen,VERDE , [0,100],[100,100],5 )


#este metodo es para actuzalizar pantalla  
    pygame.display.flip()
