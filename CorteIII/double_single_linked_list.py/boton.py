import pygame
import pruebaboton


        #pygame.display.set_caption("Animals Pirata")
def draw_button(self):

    global clicked
    action = False

    # get mouse position
    pos = pygame.mouse.get_pos()

    # create pygame Rect object for the button
    button_rect = pygame.Rect(self.x, self.y, self.width, self.height)

    # check mouseover and clicked conditions
    if button_rect.collidepoint(pos):
        if pygame.mouse.get_pressed()[0] == 1:
            clicked = True
            pygame.draw.rect(screen, self.click_col, button_rect)
        elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
            clicked = False
            action = True
        else:
            pygame.draw.rect(_Screen, self.hover_col, button_rect)
    else:
        pygame.draw.rect(screen, self.button_col, button_rect)

        def draw_button(self):

                global clicked
    
    # get mouse position
    pos = pygame.mouse.get_pos()

    # create pygame Rect object for the button
    button_rect = Rect(self.x, self.y, self.width, self.height)

    # check mouseover and clicked conditions
    hover = button_rect.collidepoint(pos)
    if hover and pygame.mouse.get_pressed()[0] == 1:
        clicked = not clicked

    color = self.button_col
    if clicked:
        color = self.click_col
    elif hover:
        color = self.hover_col

    pygame.draw.rect(screen, color, button_rect)