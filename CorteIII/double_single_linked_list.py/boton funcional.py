import pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#RED =(255,0,0 )
# Set screen dimensions
screen_width = 640
screen_height = 480

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("proyecto final") #nombre en la parte posterior del proyecto

# Set font
font = pygame.font.Font(None, 36)

# Set text
text = font.render("Button 1 clicked!", True, BLACK)          # primer boton
text2 = font.render("Button 2 clicked!", True, BLACK)       #segundo boton 

text3=  font.render("Button 3 clicked!",True,BLACK)          #tercer boton creado 

# Set button dimensions and position
button_width = 320 #---------------dimencion de los botones 
button_height = 50 #---------------dimencion de los botones
button1_x = (screen_width // 2) - (button_width // 2) #boton 1 
button1_y = (screen_height // 2) - (button_height // 2) -50


button2_x = (screen_width // 2) - (button_width // 2)  #boton 2 
button2_y = (screen_height // 2) - (button_height // 2) + 50



button3_x = (screen_width // 2) - (button_width // 2)  
button3_y = (screen_height // 2) - (button_height // 2) -10 #nuevo creado 



# Set button text
button_text = font.render("Single Linked List", True, BLACK)#primer boton 
button_text2 = font.render("Double Single Linked List", True, BLACK)#segundo boton 
button_text3 = font.render("Double Single Linked List", True, BLACK)#segundo boton 
# Set button text position
text_x = button1_x + (button_width // 2) - (button_text.get_width() // 2)
text_y = button1_y + (button_height // 2) - (button_text.get_height() // 2)
text2_x = button2_x + (button_width // 2) - (button_text2.get_width() // 2)
text2_y = button2_y + (button_height // 2) - (button_text2.get_height() // 2)
text3_x = button3_x + (button_width // 2) - (button_text2.get_width() // 2) #del boton tres 
text3_y = button3_y + (button_height // 2) - (button_text2.get_height() // 2)

# Set initial button state
button1_clicked = False
button2_clicked = False
button3_clicked = False


# Run game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if button was clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= button1_x and mouse_x <= button1_x + button_width and mouse_y >= button1_y and mouse_y <= button1_y + button_height:
                button1_clicked = True
            elif mouse_x >= button2_x and mouse_x <= button2_x + button_width and mouse_y >= button2_y and mouse_y <= button2_y + button_height:
                button2_clicked = True

    # Clear screen
    screen.fill(WHITE)

    # Draw button
    pygame.draw.rect(screen, BLACK, [button1_x, button1_y, button_width, button_height], 2)
    screen.blit(button_text, (text_x, text_y))
    pygame.draw.rect(screen, BLACK, [button2_x, button2_y, button_width, button_height], 2)#cambiar color
    screen.blit(button_text2, (text2_x, text2_y))
    pygame.draw.rect(screen, BLACK, [button3_x, button3_y, button_width, button_height], 2)#tercer boton 
    screen.blit(button_text2, (text3_x, text3_y))
    


    # Draw text if button was clicked
    if button1_clicked:
        screen.blit(text, ((screen_width // 2) - (text.get_width() // 2), screen_height - 100))
    if button2_clicked:
        screen.blit(text2, ((screen_width // 2) - (text2.get_width() // 2), screen_height - 50))
    
    if button3_clicked:
        screen.blit(text2, ((screen_width // 2) - (text2.get_width() // 2), screen_height - 50)) #boton tres 

    # Update screen
    pygame.display.flip()

# Quit game
pygame.quit()
