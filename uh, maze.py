"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
 
From:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example
 
Explanation video: http://youtu.be/8IRyt7ft7zg
 
Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/
"""
 
import pygame
 
# -- Global constants
 
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
YELLOW = (255,255,0)
RED = (255,0,0)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Coin(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.height = 15
        self.width = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(YELLOW)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()

win_list = pygame.sprite.Group()

coin_list = pygame.sprite.Group()

invis_list = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall1 = Wall(50,100,200,10)
wall_list.add(wall1)
all_sprite_list.add(wall1)

wall2 = Wall(100,0,10,100)
wall_list.add(wall2)
all_sprite_list.add(wall2)

wall3 = Wall(110,200,10,100)
wall_list.add(wall3)
all_sprite_list.add(wall3)

wall4 = Wall(190,200,10,100)
wall_list.add(wall4)
all_sprite_list.add(wall4)

wall5 = Wall(190,200,100,10)
wall_list.add(wall5)
all_sprite_list.add(wall5)

wall6 = Wall(190,300,150,10)
wall_list.add(wall6)
all_sprite_list.add(wall6)

wall7 = Wall(110,300,10,100)
wall_list.add(wall7)
all_sprite_list.add(wall7)

wall8 = Wall(55,250,10,150)
wall_list.add(wall8)
all_sprite_list.add(wall8)

wall9 = Wall(55,400,65,10)
wall_list.add(wall9)
all_sprite_list.add(wall9)

wall10 = Wall(0,475,100,10)
wall_list.add(wall10)
all_sprite_list.add(wall10)

wall = Wall(790, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(0, 590, 800, 10)
wall_list.add(wall)
all_sprite_list.add(wall)

wall11 = Wall(175,475,100,10)
wall_list.add(wall11)
all_sprite_list.add(wall11)

wall12 = Wall(100,475,10,60)
wall_list.add(wall12)
all_sprite_list.add(wall12)

wall13 = Wall(35,525,75,10)
wall_list.add(wall13)
all_sprite_list.add(wall13)

wall14 = Wall(180,525,10,100)
wall_list.add(wall14)
all_sprite_list.add(wall14)

wall15 = Wall(285,200,100,10)
wall_list.add(wall15)
all_sprite_list.add(wall15)

wall16 = Wall(285,300,100,10)
wall_list.add(wall16)
all_sprite_list.add(wall16)

wall17 = Wall(225,250,160,10)
wall_list.add(wall17)
all_sprite_list.add(wall17)

wall18 = Wall(175,375,210,10)
wall_list.add(wall18)
all_sprite_list.add(wall18)

wall19 = Wall(375,305,10,80)
wall_list.add(wall19)
all_sprite_list.add(wall19)

wall20 = Wall(190,475,210,10)
wall_list.add(wall20)
all_sprite_list.add(wall20)

wall21 = Wall(250,380,10,50)
wall_list.add(wall21)
all_sprite_list.add(wall21)

wall22 = Wall(300,0,10,150)
wall_list.add(wall22)
all_sprite_list.add(wall22)

wall23 = Wall(100,150,210,10)
wall_list.add(wall23)
all_sprite_list.add(wall23)

wall24 = Wall(375,80,10,130)
wall_list.add(wall24)
all_sprite_list.add(wall24)

wall25 = Wall(375,70,210,10)
wall_list.add(wall25)
all_sprite_list.add(wall25)

wall26 = Wall(575,70,10,100)
wall_list.add(wall26)
all_sprite_list.add(wall26)

wall27 = Wall(475,70,10,200)
wall_list.add(wall27)
all_sprite_list.add(wall27)

wall28 = Wall(425,150,50,10)
wall_list.add(wall28)
all_sprite_list.add(wall28)

wall29 = Wall(375,150,10,100)
wall_list.add(wall29)
all_sprite_list.add(wall29)

wall30 = Wall(375,200,50,10)
wall_list.add(wall30)
all_sprite_list.add(wall30)

wall31 = Wall(475,325,10,100)
wall_list.add(wall31)
all_sprite_list.add(wall31)

wall32 = Wall(475,325,75,10)
wall_list.add(wall32)
all_sprite_list.add(wall32)

wall33 = Wall(725,500,10,100)
wall_list.add(wall33)
all_sprite_list.add(wall33)

wall34 = Wall(625,500,100,10)
wall_list.add(wall34)
all_sprite_list.add(wall34)

wall35 = Wall(625,400,10,100)
wall_list.add(wall35)
all_sprite_list.add(wall35)

wall36 = Wall(700,200,100,10)
wall_list.add(wall36)
all_sprite_list.add(wall36)

wall37 = Wall(700,200,10,200)
wall_list.add(wall37)
all_sprite_list.add(wall37)

wall38 = Wall(390,480,10,150)
wall_list.add(wall38)
all_sprite_list.add(wall38)

wall39 = Wall(180,525,150,10)
wall_list.add(wall39)
all_sprite_list.add(wall39)

wall40 = Wall(475,500,150,10)
wall_list.add(wall40)
all_sprite_list.add(wall40)

wall41 = Wall(625,200,10,100)
wall_list.add(wall41)
all_sprite_list.add(wall41)

wall42 = Wall(625,250,75,10)
wall_list.add(wall42)
all_sprite_list.add(wall42)

wall43 = Wall(700,100,100,10)
wall_list.add(wall43)
all_sprite_list.add(wall43)

wall44 = Wall(380,350,100,10)
wall_list.add(wall44)
all_sprite_list.add(wall44)

wall45 = Wall(475,400,160,10)
wall_list.add(wall45)
all_sprite_list.add(wall45)

inviswall = Wall(600,450,10,10)
all_sprite_list.add(inviswall)
invis_list.add(inviswall)
inviswall.image.fill(BLACK)



win_block = Wall(735,540,55,50)
all_sprite_list.add(win_block)
win_list.add(win_block)
win_block.image.fill(WHITE)

coin1 = Coin(25,150)
all_sprite_list.add(coin1)
coin_list.add(coin1)

coin2 = Coin(350,100)
all_sprite_list.add(coin2)
coin_list.add(coin2)

coin3 = Coin(500,450)
all_sprite_list.add(coin3)
coin_list.add(coin3)

coin4 = Coin(150,300)
all_sprite_list.add(coin4)
coin_list.add(coin4)

coin5 = Coin(600,100)
all_sprite_list.add(coin5)
coin_list.add(coin5)

coin6 = Coin(25,500)
all_sprite_list.add(coin6)
coin_list.add(coin6)

coin7 = Coin(750,450)
all_sprite_list.add(coin7)
coin_list.add(coin7)
# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
 
all_sprite_list.add(player)

end_num = 0

score=0

hit=0
 
clock = pygame.time.Clock()
 
done = False
 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)
    
            

                


        end_list = pygame.sprite.spritecollide(player, win_list, False)


        for x in end_list:
            end_num += 1
            print(end_num)


        coins_collected = pygame.sprite.spritecollide(player, coin_list, True)

        for x in coins_collected:
            score += 1

        collided = pygame.sprite.spritecollide(player, invis_list, True)

        for x in collided:
            hit +=1
        
            
        
        
 
    all_sprite_list.update()
 
    screen.fill(BLACK)
 
    all_sprite_list.draw(screen)

    if end_num >0:
        font = pygame.font.SysFont("Arial", 30, True, False)
        rendered_font = font.render("You Win!", True, BLACK)
        screen.blit(rendered_font, [400,20])
        player.change_x = 0
        player.change_y = 0
        #screen.fill(WHITE)
        screen.blit(rendered_font, [400,20])

    font = pygame.font.SysFont("Arial", 30, True, False)
    rendered_font2 = font.render("Score: " + str(score), True, WHITE)
    screen.blit(rendered_font2, [100,20])
    if end_num >0:
        font = pygame.font.SysFont("Arial", 30, True, False)
        rendered_font2 = font.render("Score: " + str(score), True, RED)
        screen.blit(rendered_font2, [100,20])

    if hit == 1:
        font = pygame.font.SysFont("Arial", 30, True, False)
        rendered_font2 = font.render("You found me.", True, WHITE)
        screen.blit(rendered_font2, [300,300])
        punishment = Wall(475,400,10,100)
        wall_list.add(punishment)
        all_sprite_list.add(punishment)
        
        
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
