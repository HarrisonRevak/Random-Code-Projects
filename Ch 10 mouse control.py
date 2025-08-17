import pygame
x=188
y=140
def alien(x,y):
    pygame.draw.ellipse(screen,GREEN,[x,y,25,50])
    pygame.draw.line(screen,GREEN,[x+12,y+40],[x+12,y+90],1)
    pygame.draw.line(screen,GREEN,[x+12,y+40],[x+13,y+90],1)
    pygame.draw.line(screen,GREEN,[x+12,y+40],[x+37,y+90],1)
    pygame.draw.line(screen,GREEN,[x+12,y+90],[x+2,y+140],1)
    pygame.draw.line(screen,GREEN,[x+12,y+90],[x+22,y+140],1)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DARK_GREEN = (1,50,32)


 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False

pygame.mouse.set_visible(0)
 
clock = pygame.time.Clock()



a_change= 1
b_change= 1
c_change= 3

a=4
b=4
c=4

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    if a >= 250:
        a_change*=-1
    if b >= 250:
        b_change*=-1
    if c >= 250:
        c_change*=-1
    if a<=3:
        a_change*=-1
    if b<=3:
        b_change*=-1
    if c<=3:
        c_change*=-1


    a += a_change
    b += b_change
    c += c_change

    COLOR = (a, b, c)

    pos = pygame.mouse.get_pos()

    x = pos[0]

    y = pos[1]

    screen.fill(COLOR)

    alien(x,y)


    
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
