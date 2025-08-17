import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
NAVY_BLUE = (28, 48, 92)

YELLOW = (252,211,3)
LIME_GREEN = (174, 232, 14)
ORANGE = (255,162,0)
PINK = (255,0,230)
MAGENTA = (181,45,102)



 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(NAVY_BLUE)
    pygame.draw.line(screen, RED, [0, 0], [450, 500], 1)
    pygame.draw.line(screen, WHITE, [0, 0], [500, 500], 1)
    pygame.draw.line(screen, YELLOW, [0, 0], [550, 500], 1)
    pygame.draw.line(screen, LIME_GREEN, [0, 0], [600, 500], 1)
    pygame.draw.line(screen, ORANGE, [0, 0], [650, 500], 1)
    pygame.draw.line(screen, PINK, [0, 0], [400, 500], 1)
    pygame.draw.line(screen, MAGENTA, [0, 0], [350, 500], 1)
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
