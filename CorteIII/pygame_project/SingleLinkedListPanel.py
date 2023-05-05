from Botones.TextButton import TextButton
from Botones.TriangleButton import TriangleButton
from Botones.CircleButton import CircleButton
from Botones.RectangleButton import RectangleButton
from SLLActionPanel import SllActionPanel
from single_linked_list import SingleLinkedList
import pygame
class SLLPanel:

    def __init__(self, font):
        self.singlell = SingleLinkedList()

        self.font = font
        self.labelValue = font.render("Value Selection",True,(255,255,255))
        boton_triangle = TriangleButton((480,150))
        boton_rectangle = RectangleButton((330, 150))
        boton_circle = CircleButton((630, 150))
        self.figure_buttons_list = [boton_triangle,boton_rectangle,boton_circle]

        self.boton_sel = TextButton("Selección de acciones",40,(305, 250))

        self.action_panel = SllActionPanel(self.font, self.singlell)
        self.draw_action_panel = False

        
    def draw_panel(self, screen, mouse_pos):
        for figure in self.figure_buttons_list:
            figure.draw(screen)

        screen.blit(self.labelValue,(375,100))
        self.boton_sel.draw(screen, mouse_pos)

        if self.draw_action_panel:
            self.action_panel.draw(screen)
            self.draw_action_panel = False
        self.draw_singlell(screen)
            
    def click_event(self, mouse_pos):
        for figure in self.figure_buttons_list:
            if figure.is_mouse_contained(mouse_pos):
                self.toggle_figure_selection()
                figure.toggle_selected()
        if self.boton_sel.is_mouse_contained(mouse_pos):
            for figure in self.figure_buttons_list:
                if figure.selected:
                    self.action_panel.set_selected_figure(figure.value)
                    self.draw_action_panel = True
                    break
        
    def toggle_figure_selection(self):
        for figure in self.figure_buttons_list:
            figure.set_selected_false()
    
    def draw_singlell(self, screen):
        x_pos = 510 - (self.singlell.get_list_lenght()*65 + 15*(self.singlell.get_list_lenght()-1))//2
        for nodo in self.singlell.show_list():
            if nodo == 0:
                pygame.draw.rect(screen,(0,0,255), pygame.Rect(x_pos , 400, 65, 65), 3)
                pygame.draw.circle(screen, (0, 0, 255),(((x_pos+(x_pos+65))/2),((400+(400+65))/2)), 25, 3)
            if nodo == 1:
                pygame.draw.rect(screen,(0,255,0), pygame.Rect(x_pos , 400, 65, 65),3)
                pygame.draw.rect(screen, (0,255, 0),  pygame.Rect(x_pos+10 , 400+10, 65-20, 65-20), 3)
            if nodo == 2:
                pygame.draw.rect(screen,(255,0,0), pygame.Rect(x_pos , 400, 65, 65), 3)
                pygame.draw.polygon(screen, (255, 0, 0), ((x_pos+10,400+65-10),(x_pos+10+((65-20)/2),400+10),(x_pos-10+65,400+65-10)),3)
            x_pos+=80

