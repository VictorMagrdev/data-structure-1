import pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set screen dimensions
screen_width = 640
screen_height = 480

# Create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Button Example")

# Set font
font = pygame.font.Font(None, 36)

# Set text
text1 = font.render("Button 1 clicked!", True, BLACK)
text2 = font.render("Button 2 clicked!", True, BLACK)
text3 = font.render("Button 3 clicked!", True, BLACK)
text4 = font.render("Button 4 clicked!", True, BLACK)
text5 = font.render("Button 5 clicked!", True, BLACK)

# Set button dimensions and position
button_width = 150
button_height = 50
button1_x = (screen_width // 2) - (button_width // 2)
button1_y = (screen_height // 2) - (button_height // 2) - 100
button2_x = (screen_width // 2) - (button_width // 2)
button2_y = (screen_height // 2) - (button_height // 2) - 50
button3_x = (screen_width // 2) - (button_width // 2)
button3_y = (screen_height // 2) - (button_height // 2)
button4_x = (screen_width // 2) - (button_width // 2)
button4_y = (screen_height // 2) - (button_height // 2) + 50
button5_x = (screen_width // 2) - (button_width // 2)
button5_y = (screen_height // 2) - (button_height // 2) +100

# Set button text
button_text1 = font.render("Click me!", True, BLACK)
button_text2 = font.render("Click me too!", True, BLACK)
button_text3 = font.render("Click me three!", True, BLACK)
button_text4 = font.render("Click me four!", True, BLACK)
button_text5 = font.render("Click me five!", True, BLACK)

# Set button text position
text1_x = button1_x + (button_width // 2) - (button_text1.get_width() // 2)
text1_y = button1_y + (button_height // 2) - (button_text1.get_height() // 2)
text2_x = button2_x + (button_width // 2) - (button_text2.get_width() // 2)
text2_y = button2_y + (button_height // 2) - (button_text2.get_height() // 2)
text3_x = button3_x + (button_width // 2) - (button_text3.get_width() //2)
text3_y=button3_y+(button_width //2 )-(button_text3.get_height()//2)
text4_x = button4_x + (button_width // 2) - (button_text4.get_width() // 2)
text4_y=button4_y+(button_width //2 )-(button_text4.get_height()//2)
text5_x = button5_x + (button_width // 2) - (button_text5.get_width() // 2)
text5_y=button5_y+(button_width //2 )-(button_text5.get_height()//2)

options = ["Option 1", "Option 2","Option 3", "Option 4","Option 5"]
option_height = 30

# run game lop nueva prueba 

running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # Check if button was clicked

            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= button3_x and mouse_x <= button3_x + button_width and mouse_y >= button3_y and mouse_y <= button3_y + button_height:
                button_clicked = not button_clicked
            elif button_clicked:
                # Check if option was selected
                for i in range(len(options)):
                    option_x = button3_x
                    option_y = button3_y + button_height + (i * option_height)
                    if mouse_x >= option_x and mouse_x <= option_x + button_width and mouse_y >= option_y and mouse_y <= option_y + option_height:
                        option_selected = i



# Clear screen
    screen.fill(WHITE)




    # Draw button
    pygame.draw.rect(screen, BLACK, [button1_x, button1_y, button_width, button_height], 1)#1
    screen.blit(button_text1, (text1_x, text1_y))
    pygame.draw.rect(screen, RED, [button2_x, button2_y, button_width, button_height], 2)#cambiar color del segundo boton
    screen.blit(button_text2, (text2_x, text2_y))
    pygame.draw.rect(screen, BLACK, [button3_x, button3_y, button_width, button_height], 3) # 3 
    screen.blit(button_text3, (text2_x, text3_y))
    pygame.draw.rect(screen, BLACK, [button4_x, button4_y, button_width, button_height], 3) #4 
    screen.blit(button_text4, (text4_x, text4_y))
    pygame.draw.rect(screen, BLACK, [button5_x, button5_y, button_width, button_height], 3) #5
    screen.blit(button_text5, (text5_x, text5_y))
    





    # Draw text if button was clicked
    if button_clicked:
        for i in range(len(options)):
            option_x = button3_x
            option_y = button3_y + button_height + (i * option_height)
            pygame.draw.rect(screen, BLACK, [option_x, option_y, button_width, option_height], 2)
            option_text = font.render(options[i], True, BLACK)
            screen.blit(option_text,
                        (option_x + (button_width // 2) - (option_text.get_width() // 2),
                         option_y + (option_height // 2) - (option_text.get_height() // 2)))
            
            
    # Draw text if option was selected
    if option_selected is not None:
        if option_selected == 0:
            screen.blit(text1,
                        ((screen_width // 2) - (text1.get_width() // 2), screen_height - text1.get_height()))
        elif option_selected == 1:
            screen.blit(text2,
                        ((screen_width // 2) - (text2.get_width() // 2), screen_height - text2.get_height()))
        elif option_selected == 2:
            screen.blit(text3,
                        ((screen_width // 2) - (text3.get_width() // 2), screen_height - text3.get_height()))












    # Update screen
pygame.display.flip()

# Quit game
pygame.quit()

