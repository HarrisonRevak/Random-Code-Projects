"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DGREEN = (47, 156, 76)
MOON = (209, 209, 209)
SUN = (255, 234, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
a = 550
b = 75
c = 250
d = 500
e=15
x = 0
y = 0
z = 0

achange = 2
bchange = 3
cchange = -1
dchange = -3
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    color = (x,y,z)
    a += achange
    b += bchange
    c += cchange
    d += dchange
    e += 1
    y +=2
    z +=5
    if d == 150 or d<150:
        dchange = -2
    if d == 0 or d<0:
        d=0
    if c == 0 or c<0:
        c=0
    if e == 75 or e>75:
        e=75
    if y == 222 or y>222:
        y=222
    if z == 255 or z>255:
        z=255
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(color)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, DGREEN,[0,400,700,200])
    pygame.draw.circle(screen,MOON,[a,b],25)
    pygame.draw.circle(screen,SUN,[c,d],e)
    






    pygame.draw.rect(screen, DGREEN,[0,400,700,200])
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
