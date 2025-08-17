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
SUN = (253,184,19)
 
pygame.init()
class Ball:
    def __init__(self):
        #Ball position
        self.x=0
        self.y=0

        #Ball's Vector
        self.change_x=2
        self.change_y=1

        #Ball size
        self.size=10

        #ball color
        self.color=[255,255,255]

    def move(self):
        self.x+=self.change_x
        self.y+=self.change_y

    def draw(self):
        pygame.draw.circle(screen, self.color, [self.x,self.y], self.size)

 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

volleyball = Ball()
beach = Ball()
sun = Ball()
beach.size=20
beach.x=100
beach.y=0
beach.color=[255,0,0]
beach.change_x=5
beach.change_y=10
sun.color=[253,184,19]
sun.size=100
sun.change_x=0
sun.change_y=0


 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here

    volleyball.draw()
    volleyball.move()
    beach.draw()
    beach.move()
    sun.draw()
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
