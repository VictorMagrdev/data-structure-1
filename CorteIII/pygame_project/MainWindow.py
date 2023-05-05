import pygame
from MenuPanel import MenuPanel
from SingleLinkedListPanel import SLLPanel
from temp_panel import tempPanel
import sys
class Window:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,600))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.font = pygame.font.SysFont("Helvetica",40)

        self.sll_panel = SLLPanel(self.font)
        self.temppanel = tempPanel()
        self.current_panel = self.sll_panel
        self.run_window()

    def run_window(self):
        menu_panel = MenuPanel()

        run = True
        while run:

            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.change_current_panel(menu_panel.click_event(mouse_pos))
                    self.current_panel.click_event(mouse_pos)
            
            self.screen.fill((0,0,0))
            self.current_panel.draw_panel(self.screen, mouse_pos)
            menu_panel.draw_menu_panel(self.screen, mouse_pos)
            pygame.display.update()
        

    def change_current_panel(self, panel_name):
        if panel_name == "SingleLL":
            self.current_panel = self.sll_panel
        elif panel_name == "DoubleLL":
            self.current_panel = self.temppanel
        elif panel_name == "Pilas y Colas":
            self.current_panel = self.temppanel
        elif panel_name == "Arboles":
            self.current_panel = self.temppanel
        elif panel_name == "Grafos":
            self.current_panel = self.temppanel
    

inita = Window()
inita.run_window()