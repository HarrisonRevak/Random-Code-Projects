
import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WEIRDGREEN = (46, 148, 88)
PURPLE = (111, 74, 199)
VIOLET = (33, 5, 99)
NAVY_BLUE = (29,87,140)

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


 
	pygame.display.flip()
 
	clock.tick(60)
 
pygame.quit()
