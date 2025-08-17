import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN=(150,75,0)
ORANGE=(255,165,0)
PRETTY_ORANGE=(255,229,180)
YELLOW=(255,255,0)
 
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
    
   

    pygame.draw.circle(screen, BROWN, [325,375], 100) #body
    pygame.draw.circle(screen, BROWN, [325,250], 70) #head
    pygame.draw.circle(screen, BLACK, [340,230], 5) #eye
    pygame.draw.circle(screen, BLACK, [310,230], 5) #eye
    pygame.draw.circle(screen, WHITE, [300,225], 25) #eye
    pygame.draw.circle(screen, WHITE, [350,225], 25) #eye  
    pygame.draw.polygon(screen, ORANGE, [[310,260], [340,260], [325,300]]) #beak
    pygame.draw.ellipse(screen, RED, [340,260,15,45]) #wattle
    pygame.draw.circle(screen, RED, [340,260], 10) #wattle
    pygame.draw.line(screen, YELLOW, [375,450], [400,480], 30) #foot
    pygame.draw.line(screen, YELLOW, [275,450], [250,480], 30) #foot
 

    pygame.draw.circle(screen, ORANGE, [325,400], 300) #feather
    pygame.draw.circle(screen, YELLOW, [325,400], 250) #feathers
    pygame.draw.circle(screen, PRETTY_ORANGE, [325,400], 200) #feathers

  
    pygame.draw.rect(screen, WHITE, [0,400,700,110]) #feather cover
    pygame.draw.line(screen, BLACK, [325,375], [325,100], 1) #middle line
    pygame.draw.line(screen, BLACK, [325,375], [100,200], 1) #line
    pygame.draw.line(screen, BLACK, [325,375], [550,200], 1) #line
    pygame.draw.line(screen, BLACK, [325,375], [45,300], 1) #line
    pygame.draw.line(screen, BLACK, [325,375], [605,300], 1) #line
    pygame.draw.line(screen, BLACK, [325,375], [190,135], 1) #line
    pygame.draw.line(screen, BLACK, [325,375], [460,135], 1) #line

    pygame.draw.line(screen, YELLOW, [375,450], [400,480], 30) #foot

    pygame.draw.line(screen, YELLOW, [275,450], [250,480], 30) #foot

    pygame.draw.circle(screen, BROWN, [325,375], 100) #body
    pygame.draw.circle(screen, BROWN, [325,250], 70) #head

    pygame.draw.ellipse(screen, RED, [340,260,15,45]) #wattle
    pygame.draw.circle(screen, RED, [340,260], 10) #wattle

    pygame.draw.polygon(screen, ORANGE, [[310,260], [340,260], [325,300]]) #beak


    
    pygame.draw.circle(screen, WHITE, [300,225], 25) #eye
    pygame.draw.circle(screen, WHITE, [350,225], 25) #eye
    pygame.draw.circle(screen, BLACK, [340,230], 5) #eye
    pygame.draw.circle(screen, BLACK, [310,230], 5) #eye




 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
