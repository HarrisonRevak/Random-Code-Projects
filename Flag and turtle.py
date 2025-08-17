import pygame


def netherland(x,y):
    pygame.draw.rect(screen, RED, (x,y+50,250,50))
    pygame.draw.rect(screen, WHITE,(x,y+100,250,50))
    pygame.draw.rect(screen, BLUE, (x,y+150,250,50))

def turtle(x,y):
    pygame.draw.ellipse(screen, GREEN,(a+100,b,50,100))
    pygame.draw.ellipse(screen, GREEN,(a+100,b+100,50,100))
    pygame.draw.ellipse(screen, GREEN,(a+125,b+75,50,50))
    pygame.draw.ellipse(screen, GREEN,(a,b,50,100))
    pygame.draw.ellipse(screen, GREEN,(a,b+100,50,100))
    pygame.draw.circle(screen, BROWN,(a+75,b+100), 75)




BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
NAVY_BLUE = (28, 48, 92)
BROWN = (160,95,53)

YELLOW = (252,211,3)
LIME_GREEN = (174, 232, 14)
ORANGE = (255,162,0)
PINK = (255,0,230)
MAGENTA = (181,45,102)

x=100
y=100
a=100
b=100

 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False

x_coord = 100
y_coord = 100

x_speed=0
y_speed=0

 
clock = pygame.time.Clock()
 
while not done:
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
            
    x_coord += x_speed
    y_coord += y_speed


    pos = pygame.mouse.get_pos()

    a = pos[0]

    b = pos[1]


    screen.fill(BLACK)

    netherland(x_coord,y_coord)


    turtle(a,b)


    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
