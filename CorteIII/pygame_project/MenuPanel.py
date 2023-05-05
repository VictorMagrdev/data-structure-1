
from Botones.TextButton import TextButton
class MenuPanel:

    def __init__(self):
        boton_sll = TextButton("SingleLL",40,(20,10))
        boton_dll = TextButton("DoubleLL",40,(210, 10))
        boton_pyl = TextButton("Pilas y Colas",40,(415, 10))
        boton_arb = TextButton("Arboles",40,(680, 10))
        boton_grf = TextButton("Grafos",40,(850, 10))
        self.lista_botones = [boton_sll,boton_dll,boton_pyl,boton_arb,boton_grf]

    def draw_menu_panel(self, screen, mouse_pos):
        for button in self.lista_botones:
            button.draw(screen,mouse_pos)

    def click_event(self, mouse_pos):
        for button in self.lista_botones:
            if button.is_mouse_contained(mouse_pos):
                return button.text
