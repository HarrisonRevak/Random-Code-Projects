import pygame
 
def grass(grassx,grassHeight):
	if grassHeight>30:
    		grassHeight=30
	elif grassHeight<10:
    		grassHeight=10
	pygame.draw.polygon(screen, GREEN, ([grassx,500], [grassx+5, 500-grassHeight], [grassx+10,500]))
 
def cloud(cloudx, cloudy, cloudWidth):
	if cloudy>200:
    		cloudy=200
	if cloudWidth>400:
    		cloudWidth=400
	pygame.draw.ellipse(screen, WHITE, [cloudx, cloudy, cloudWidth, 70])  
 
def flower(flowerx, flowery):
	if flowery<300:
    		flowery=300
	elif flowery>450:
    		flowery=450
	pygame.draw.line(screen, GREEN, [flowerx, 500], [flowerx, flowery], 5) 
	pygame.draw.circle(screen, ORANGE, [flowerx, flowery], 20)
	pygame.draw.circle(screen, YELLOW, [flowerx, flowery], 5)
	pygame.draw.line(screen, GREEN, [flowerx, flowery+40], [flowerx+10, flowery+30],5)
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (75, 214, 140)
BLUE = (137, 215, 232)
YELLOW = (237, 229, 109)
ORANGE=(240, 157, 70)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
done = False
clock = pygame.time.Clock()

#indent the lines in the main game loop AFTER you have pasted it into python.
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLUE)

    grass(0,500)
    grass(15,500)
    grass(35,500)
    grass(50,500)
    grass(70,500)
    grass(85,500)
    grass(105,500)
    grass(120,500)
    grass(140,500)
    grass(155,500)
    grass(175,500)
    grass(190,500)
    grass(210,500)
    grass(225,500)
    grass(245,500)
    grass(260,500)
    grass(280,500)
    grass(295,500)
    grass(315,500)
    grass(330,500)
    grass(350,500)
    grass(365,500)
    grass(385,500)
    grass(400,500)
    grass(420,500)
    grass(435,500)
    grass(455,500)
    grass(470,500)
    grass(490,500)
    grass(505,500)
    grass(525,500)
    grass(540,500)
    grass(560,500)
    grass(575,500)
    grass(595,500)
    grass(610,500)
    grass(630,500)
    grass(645,500)
    grass(665,500)
    grass(680,500)
    grass(700,500)

    cloud(50,200,200)
    cloud(150,150,150)
    cloud(350,300,160)
    cloud(600,200,130)
    cloud(500,50,140)
    cloud(75,50,125)
    
    flower(50,500)
    flower(150,400)
    flower(350,420)
    flower(500,350)
    flower(600,450)
    flower(200,200)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()
