import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BRIGHTYELLOW = (255,243,96)
DARKBRIGHTYELLOW = (240,227,63)
BROWN = (180,122,61)
OTHERBLUE=(126,181,232)
SAND =(255, 211, 137)
DENIM =(18, 119, 224)
 
pygame.init()
 
size = (700, 500)
screen = pygame.display.set_mode(size)

pi=3.1415
 
pygame.display.set_caption("My Game")
 
done = False
 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(DENIM)

    pygame.draw.rect(screen, OTHERBLUE,[0,0,700,150])
    pygame.draw.rect(screen, BLUE,[0,300,700,250])
    pygame.draw.rect(screen, SAND,[0,350,700,250])

    pygame.draw.circle(screen, SAND,[675,375],75)
    pygame.draw.circle(screen, SAND,[500,380],85)
    pygame.draw.ellipse(screen, SAND,[400,250,300,200])
    pygame.draw.ellipse(screen, SAND,[50,295,150,100])
    pygame.draw.circle(screen, SAND,[200,375],100)
    pygame.draw.circle(screen, SAND,[50,345],50)
    
    
    pygame.draw.rect(screen, BRIGHTYELLOW,[250,50,200,200])
    pygame.draw.rect(screen, WHITE,[250,200,200,25])
    pygame.draw.rect(screen, BROWN,[250,225,200,50])
    pygame.draw.rect(screen, WHITE,[250,200,200,25])


    pygame.draw.rect(screen, BRIGHTYELLOW,[297,280,10,100])
    pygame.draw.rect(screen, BRIGHTYELLOW,[393,280,10,100])

    pygame.draw.rect(screen, BROWN,[287,275,30,15])
    pygame.draw.circle(screen, BROWN,[302,280],15)
    pygame.draw.circle(screen, BROWN,[398,280],15)
    pygame.draw.rect(screen, BROWN,[383,275,30,15])

    pygame.draw.rect(screen, WHITE,[297,320,10,60])
    pygame.draw.rect(screen, WHITE,[393,320,10,60])
    pygame.draw.rect(screen, OTHERBLUE,[297,330,10,5])
    pygame.draw.rect(screen, OTHERBLUE,[393,330,10,5])
    pygame.draw.rect(screen, RED,[393,340,10,5])
    pygame.draw.rect(screen, RED,[297,340,10,5])

    pygame.draw.rect(screen, BLACK,[260,375,50,30])
    pygame.draw.circle(screen, BLACK,[270,385],22)
    pygame.draw.circle(screen, BLACK,[280,385],18)
    pygame.draw.circle(screen, BLACK,[290,390],14)
    pygame.draw.ellipse(screen, WHITE,[260,370,20,10])
    pygame.draw.circle(screen, BLACK,[310,390],17)

    pygame.draw.rect(screen, BLACK, [390,375,50,30])
    pygame.draw.circle(screen, BLACK,[430,385],22)
    pygame.draw.circle(screen, BLACK,[420,385],18)
    pygame.draw.circle(screen, BLACK,[410,390],14)
    pygame.draw.ellipse(screen, WHITE,[420,370,20,10])
    pygame.draw.circle(screen, BLACK,[390,390],17)
                             

    pygame.draw.ellipse(screen, DARKBRIGHTYELLOW,[265,65,25,20])
    pygame.draw.ellipse(screen, DARKBRIGHTYELLOW,[255,85,15,15])
    
    pygame.draw.rect(screen, BLACK,[260,250,35,10])
    pygame.draw.rect(screen, BLACK,[310,250,35,10])
    pygame.draw.rect(screen, BLACK,[355,250,35,10])
    pygame.draw.rect(screen, BLACK,[405,250,35,10])
    
    pygame.draw.line(screen, BLACK,[280,200],[315,215],1)
    pygame.draw.line(screen, BLACK,[315,215],[320,200],1)

    pygame.draw.line(screen, BLACK,[420,200],[385,215],1)
    pygame.draw.line(screen, BLACK,[385,215],[380,200],1)

    pygame.draw.rect(screen, RED,[340,200,20,70])
    pygame.draw.rect(screen, RED,[335,200,30,20])
    pygame.draw.circle(screen, RED,[350,210],15)
    pygame.draw.circle(screen, RED,[349,210],15)
    pygame.draw.circle(screen, RED,[351,210],15)


    pygame.draw.rect(screen, BRIGHTYELLOW,[460,180,10,100])
    pygame.draw.rect(screen, BRIGHTYELLOW,[230,180,10,100])

    pygame.draw.circle(screen, BRIGHTYELLOW,[235,275],20)
    pygame.draw.circle(screen, BRIGHTYELLOW,[465,275],20)

    pygame.draw.circle(screen, WHITE,[240,180],15)
    pygame.draw.rect(screen, WHITE,[225,180,30,25])
    pygame.draw.circle(screen, WHITE,[460,180],15)
    pygame.draw.rect(screen, WHITE,[445,180,30,25])

    
    

    pygame.draw.circle(screen, BRIGHTYELLOW,[280,195],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[260,190],20)
    pygame.draw.circle(screen, BRIGHTYELLOW,[300,195],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[440,190],20)
    pygame.draw.circle(screen, BRIGHTYELLOW,[350,190],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[375,195],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[340,190],17)
    pygame.draw.circle(screen, BRIGHTYELLOW,[330,190],14)
    pygame.draw.circle(screen, BRIGHTYELLOW,[385,190],18)
    pygame.draw.circle(screen, BRIGHTYELLOW,[420,190],17)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,50],20)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,50],20)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,180],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,175],17)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,160],16)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,150],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,145],19)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,135],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,120],13)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,110],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,100],17)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,90],18)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,80],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,70],16)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,60],13)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,200],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,190],12)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,180],19)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,170],12)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,160],16)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,150],13)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,140],14)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,130],18)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,120],17)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,110],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,100],14)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,90],18)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,80],13)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,70],17)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,60],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[250,50],18)
    pygame.draw.circle(screen, BRIGHTYELLOW,[260,50],18)
    pygame.draw.circle(screen, BRIGHTYELLOW,[270,50],13)
    pygame.draw.circle(screen, BRIGHTYELLOW,[290,50],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[300,50],12)
    pygame.draw.circle(screen, BRIGHTYELLOW,[310,50],16)
    pygame.draw.circle(screen, BRIGHTYELLOW,[320,50],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[330,50],13)
    pygame.draw.circle(screen, BRIGHTYELLOW,[340,50],19)
    pygame.draw.circle(screen, BRIGHTYELLOW,[350,50],17)
    pygame.draw.circle(screen, BRIGHTYELLOW,[360,50],14)
    pygame.draw.circle(screen, BRIGHTYELLOW,[370,50],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[380,50],12)
    pygame.draw.circle(screen, BRIGHTYELLOW,[390,50],18)
    pygame.draw.circle(screen, BRIGHTYELLOW,[400,50],18)
    pygame.draw.circle(screen, BRIGHTYELLOW,[410,50],16)
    pygame.draw.circle(screen, BRIGHTYELLOW,[420,50],17)
    pygame.draw.circle(screen, BRIGHTYELLOW,[430,50],15)
    pygame.draw.circle(screen, BRIGHTYELLOW,[440,50],14)
    pygame.draw.circle(screen, BRIGHTYELLOW,[450,50],12)
    
    


    pygame.draw.ellipse(screen, DARKBRIGHTYELLOW,[260,65,25,20])
    pygame.draw.ellipse(screen, DARKBRIGHTYELLOW,[250,85,15,15])
    pygame.draw.ellipse(screen, DARKBRIGHTYELLOW,[430,70,15,15])
    pygame.draw.ellipse(screen, DARKBRIGHTYELLOW,[270,185,20,18])
    pygame.draw.ellipse(screen, DARKBRIGHTYELLOW,[260,170,15,15])
    pygame.draw.ellipse(screen, DARKBRIGHTYELLOW,[430,170,20,20])
    pygame.draw.ellipse(screen, DARKBRIGHTYELLOW,[420,190,10,10])


    pygame.draw.rect(screen, BLACK,[295,55,10,20])
    pygame.draw.rect(screen, BLACK,[315,60,10,25])
    pygame.draw.rect(screen, BLACK,[275,60,10,25])

    pygame.draw.rect(screen, BLACK,[395,55,10,20])
    pygame.draw.rect(screen, BLACK,[410,60,10,25])
    pygame.draw.rect(screen, BLACK,[375,60,10,25])

    pygame.draw.circle(screen, BLACK,[300,115],42)
    pygame.draw.circle(screen, BLACK,[400,115],42)
    pygame.draw.ellipse(screen, WHITE,[260,75,80,80])
    pygame.draw.ellipse(screen, WHITE,[360,75,80,80])
    pygame.draw.ellipse(screen, OTHERBLUE,[285,105,40,40])
    pygame.draw.ellipse(screen, OTHERBLUE,[375,105,40,40])
    pygame.draw.circle(screen, BLACK,[305,125],10)
    pygame.draw.circle(screen, BLACK,[395,125],10)
    pygame.draw.circle(screen, WHITE,[295,110],7)
    pygame.draw.circle(screen, WHITE,[315,135],5)


    pygame.draw.ellipse(screen, BLACK,[340,125,20,20],2)
    pygame.draw.ellipse(screen, BLACK,[340,125,20,20],2)
    pygame.draw.circle(screen, BRIGHTYELLOW,[345,145],10)

   

    pygame.draw.arc(screen, BLACK, [275,120,150,50], pi,    3*pi/2, 2)
    pygame.draw.arc(screen, BLACK, [275,120,150,50], 3*pi/2,    2*pi, 2)


    pygame.draw.ellipse(screen, BRIGHTYELLOW,[255,135,40,30])
    pygame.draw.ellipse(screen, BRIGHTYELLOW,[405,135,40,30])


    
    pygame.draw.rect(screen, WHITE,[325,169,20,30])
    pygame.draw.rect(screen, WHITE,[355,169,20,30])

    
    pygame.draw.circle(screen, WHITE,[385,110],5)
    pygame.draw.circle(screen, WHITE,[405,135],5)
    
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
