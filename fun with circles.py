import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (196,84,24)
YELLOW = (246,255,0)
PINK = (255, 99, 156)
GREEN = (25, 133, 25)
BLUEE = (34, 0, 255)
PURPLE = (137, 89, 153)
 
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
 
	screen.fill(WHITE)
	
	pygame.draw.circle(screen, RED, [100,100], 50, 1)
	pygame.draw.circle(screen, BROWN, [300,100], 50, 10)
	pygame.draw.circle(screen, YELLOW, [500,100], 50)
	pygame.draw.circle(screen, PINK, [200,300], 100)
	pygame.draw.circle(screen, GREEN, [100,400], 100)
	pygame.draw.circle(screen, PURPLE, [700,500], 100)
	pygame.draw.circle(screen, BLUEE, [600,400], 50)
	
	pygame.display.flip()
 
	clock.tick(60)
 
pygame.quit()
