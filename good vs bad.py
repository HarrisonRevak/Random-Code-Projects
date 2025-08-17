"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
import random
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LB = (180,210,228)
BV = (107,50,124)

class Player(pygame.sprite.Sprite):
    def __init__(self,color,w,h):
        super().__init__()
        self.image = pygame.Surface([w,h])
        self.image.fill(color)
        self.rect = self.image.get_rect()
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

bad_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(10):
    bad = Player(RED, 30, 30)
    bad.rect.x = random.randrange(700)
    bad.rect.y = random.randrange(500)
    bad_list.add(bad)
    all_sprites_list.add(bad)

good = Player(BLACK, 20, 20)
all_sprites_list.add(good)

score=0
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here

    pos = pygame.mouse.get_pos()
    good.rect.x = pos[0]
    good.rect.y = pos[1]

    caught_list = pygame.sprite.spritecollide(good, bad_list, True)

    for a in caught_list:
        score += 1

    print_score = str(score)
    font = pygame.font.SysFont("Arial", 30, True, False)
    rendered_font = font.render("Score: " + print_score, True, BLACK)
    
     
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
    screen.blit(rendered_font, [400,20])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
