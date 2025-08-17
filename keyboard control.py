"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame


def americauhh(x,y):
    pygame.draw.rect(screen, RED,[x,y,x+400,25])
    pygame.draw.rect(screen, WHITE,[x,y+25,x+400,25])
    pygame.draw.rect(screen, RED,[x,y+50,x+400,25])
    pygame.draw.rect(screen, WHITE,[x,y+75,x+400,25])
    pygame.draw.rect(screen, RED,[x,y+100,x+400,25])
    pygame.draw.rect(screen, WHITE,[x,y+125,x+400,25])
    pygame.draw.rect(screen, RED,[x,y+150,x+400,25])
    pygame.draw.rect(screen, WHITE,[x,y+175,x+400,25])
    pygame.draw.rect(screen, RED,[x,y+200,x+400,25])
    pygame.draw.rect(screen, WHITE,[x,y+225,x+400,25])
    pygame.draw.rect(screen, RED,[x,y+250,x+400,25])
    pygame.draw.rect(screen, WHITE,[x,y+275,x+400,25])
    pygame.draw.rect(screen, RED,[x,y+300,x+400,25])
    pygame.draw.rect(screen, BLUE,[x,y,x+200,y+75])

def stickman(x,y):
    pygame.draw.circle(screen, BLACK, [x,y],25,2)
    pygame.draw.line(screen, BLACK, [x,y+25], [x,y+75],2)
    pygame.draw.line(screen, BLACK, [x,y+25], [x+25,y+75],2)
    pygame.draw.line(screen, BLACK, [x,y+25], [x-25,y+75],2)
    pygame.draw.line(screen, BLACK, [x,y+75], [x+25,y+125],2)
    pygame.draw.line(screen, BLACK, [x,y+75], [x-25,y+125],2)




    
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (211,211,211)
YELLOW = (255,255,0)
BLUE = (0,0,255)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x_coord = 100
y_coord = 100


x_speed=0
y_speed=0

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_speed=-3
            if event.key==pygame.K_RIGHT:
                x_speed=3
            if event.key==pygame.K_UP:
                y_speed=-3
            if event.key==pygame.K_DOWN:
                y_speed=3
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT:
                x_speed=0
            if event.key==pygame.K_RIGHT:
                x_speed=0
            if event.key==pygame.K_UP:
                y_speed=0
            if event.key==pygame.K_DOWN:
                y_speed=0
            
    
    # --- Game logic should go here

    x_coord += x_speed
    y_coord += y_speed


        

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    

    stickman(x_coord,y_coord)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
