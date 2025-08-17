import pygame

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
 
clock = pygame.time.Clock()

y=200

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

    screen.fill(COLOR)

    pygame.draw.rect(screen,DARK_GREEN,[0,400,700,200])
    
    pygame.draw.ellipse(screen,GREEN,[188,y-60,25,50])
    pygame.draw.line(screen,GREEN,[200,y-20],[200,y+30],1)
    pygame.draw.line(screen,GREEN,[200,y-20],[175,y+30],1)
    pygame.draw.line(screen,GREEN,[200,y-20],[225,y+30],1)
    pygame.draw.line(screen,GREEN,[200,y+30],[190,y+80],1)
    pygame.draw.line(screen,GREEN,[200,y+30],[210,y+80],1)

    pygame.draw.ellipse(screen,RED,[75,110,300,175])

    y+=1
    if y > 500:
        y=200
    
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
