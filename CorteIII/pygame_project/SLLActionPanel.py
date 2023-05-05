
from Botones.TextButton import TextButton
import pygame

class SllActionPanel:

    def __init__(self, font, singlell):
        self.font = font
        self.sll = singlell
        self.selected_figure = None
        self.labelPosicion = font.render("Position",True,(255,255,255))
        boton_a1 = TextButton("Agregar elemento al inicio", 24,(35,30))
        boton_a2 = TextButton("Agregar elemento al final", 24,(35, 90))
        boton_a3 = TextButton("Eliminar elemento al inicio", 24,(35, 150))
        boton_a4 = TextButton("Eliminar elemento al final", 24,(35, 210))
        boton_a5 = TextButton("Invertir la lista enlazada", 24,(35, 270))
        boton_a6 = TextButton("Eliminar todos los elementos", 24,(35, 330))
        boton_a7 = TextButton("Eliminar elemento en la posicion", 24,(35, 390))
        boton_a8 = TextButton("Agregar elemento a la posicion", 24,(35, 450))
        boton_a9 = TextButton("Editar elemento a la posicion",24,(35, 510))
        self.lista_acciones=[boton_a1,boton_a2,boton_a3,boton_a4,boton_a5,boton_a6,boton_a7,boton_a8,boton_a9]

    def draw(self,screen):
        run = True
        user_number = 0
        user_numberd = self.font.render("0",False,(255,255,255)) 
        while run:
            screen.fill((0,0,0))
            pygame.draw.rect(screen,(0,0,255), pygame.Rect(0, 0, 500, 1000))
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    break
                if event.type == pygame.KEYDOWN: 
                    if event.unicode.isnumeric():
                        user_numberd = self.font.render(event.unicode,True,(255,255,255)) 
                        user_number = int(event.unicode)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for boton in self.lista_acciones:
                        if boton.is_mouse_contained(mouse_pos):
                            self.edit_singlell(boton.text,user_number)
                            run = False
            for button in self.lista_acciones:
                button.draw(screen,mouse_pos)
            screen.blit(user_numberd,(750,270))
            screen.blit(self.labelPosicion,(685,200))
            pygame.display.update()
        return

    def set_selected_figure(self,figure):
        self.selected_figure = figure
    
    def edit_singlell(self, boton_text, user_number):
        if boton_text == "Agregar elemento al inicio":
            self.sll.create_node_sll_unshift(self.selected_figure) 
        elif boton_text == "Agregar elemento al final":
            self.sll.create_node_sll_ends(self.selected_figure)  
        elif boton_text == "Eliminar elemento al inicio":
            self.sll.shift_node_sll()
        elif boton_text == "Eliminar elemento al final":
            self.sll.delete_node_sll_pop()
        elif boton_text == "Invertir la lista enlazada":
            self.sll.reverse_sll()  
        elif boton_text == "Eliminar todos los elementos":
            self.sll.remove_all_nodes()  
        elif boton_text == "Eliminar elemento en la posicion":
            self.sll.remove_node(user_number)   
        elif boton_text == "Agregar elemento a la posicion":
            self.sll.insert_value_at_index( self.selected_figure,user_number)   
        elif boton_text == "Editar elemento a la posicion":
            self.sll.update_node_value(user_number,self.selected_figure)
