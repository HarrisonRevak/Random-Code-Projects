#Harrison Revak
#5/24/2024
#Computer Science 1
#New Albany High School
import random 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Slay The Dragon")

class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface([15, 15])
        self.image=pygame.image.load("Knight.png")
      

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        self.change_x = 0
        self.change_y = 0
        self.walls = None

    def changespeed(self, x, y):
        
        self.change_x += x
        self.change_y += y
        

    def update(self):

        self.rect.x += self.change_x

        did_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in did_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        did_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in did_hit_list:

            if self.change_y >0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Fireball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([15,15])
        self.image = pygame.image.load("Fireball.png")

        self.rect = self.image.get_rect()
        self.rect.y = -25
        self.rect.x = random.randrange(700)
    def update(self):
        self.rect.y +=3

        if self.rect.y >500:
            self.rect.y = -25
            self.rect.x = random.randrange(700)


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Dragon(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        super().__init__()

        self.image = pygame.Surface([25,25])
        self.image = pygame.image.load("Dragon.png")

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Breath(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([25,300])
        self.image = pygame.image.load("Fire_Breath.png")
   

        self.rect = self.image.get_rect()
        self.rect.y = -25
        self.rect.x = 0

class Shield(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([25,25])
        self.image = pygame.image.load("Shield.png")
        
        self.rect = self.image.get_rect()
        self.rect.y = (player.rect.y-20)
        self.rect.x = (player.rect.x-15)

    def update(self):
        self.rect.y = (player.rect.y-20)
        self.rect.x = (player.rect.x-15)

 
# Loop until the user clicks the close button.
done = False

dragon1 = pygame.image.load("Dragon.png")


bg = pygame.image.load("background.jpg")
bg = pygame.transform.scale(bg, (700, 500))

princess = pygame.image.load("Princess1.png")
princess = pygame.transform.scale(princess, (300,300))


all_sprite_list = pygame.sprite.Group()

fire_list = pygame.sprite.Group()

wall_list = pygame.sprite.Group()

dragon_list = pygame.sprite.Group()

coin_list = pygame.sprite.Group()

breath_list = pygame.sprite.Group()

shield_list = pygame.sprite.Group()

roar = pygame.mixer.Sound("Roar.ogg")

whoosh = pygame.mixer.Sound("Whoosh.ogg")
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

dragon = Dragon(235,-75)
all_sprite_list.add(dragon)
dragon_list.add(dragon)


breath = Breath()
breath.rect.x = 250
breath.rect.y = 0





barrier1 = Barrier(225,0,25,100)
all_sprite_list.add(barrier1)
wall_list.add(barrier1)

barrier2 = Barrier(475,0,25,100)
all_sprite_list.add(barrier2)
wall_list.add(barrier2)


defense = Barrier(200,400,200,15)
all_sprite_list.add(defense)
wall_list.add(defense)

defense2 = Barrier(150,275,50,15)
all_sprite_list.add(defense2)
wall_list.add(defense2)

defense3 = Barrier(400,275,50,15)
all_sprite_list.add(defense3)
wall_list.add(defense3)

defense4 = Barrier(0,125,75,15)
all_sprite_list.add(defense4)
wall_list.add(defense4)

defense5 = Barrier(0,275,100,15)
all_sprite_list.add(defense5)
wall_list.add(defense5)

defense7 = Barrier(500,400,75,15)
all_sprite_list.add(defense7)
wall_list.add(defense7)


defense8 = Barrier(690,0,25,100)
all_sprite_list.add(defense8)
wall_list.add(defense8)


defense9 = Barrier(650,100,75,15)
all_sprite_list.add(defense9)
wall_list.add(defense9)


coin = Barrier(200,200,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(600,225,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(50,150,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(100,400,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(425,300,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(200,225,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(500,350,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(200,100,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(450,375,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(650,125,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)

coin = Barrier(200,375,15,15)
all_sprite_list.add(coin)
coin_list.add(coin)
coin.image.fill(YELLOW)




player = Knight(300,450)
all_sprite_list.add(player)
player.walls = wall_list

    

killed = 0

dead = False

win = False

score = 0

start = False

attack = False

timer = 0
timer2 = 0

timershield = 0

held = False

breathed = False

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            #Frogger
            if event.key == pygame.K_LEFT:
                #Frogger
                player.changespeed(-3,0)
                if wall_collision:
                    player.changespeed(3,0)
       
                #Frogger
            elif event.key == pygame.K_RIGHT:
                #Frogger
                player.changespeed(3,0)
                if wall_collision:
                    player.changespeed(-3,0)
        
                #Frogger
            elif event.key == pygame.K_UP:
                #Frogger
                player.changespeed(0,-3)
                if wall_collision:
                    player.changespeed(0,3)
   
                #Frogger
            elif event.key == pygame.K_DOWN:
                #Frogger
                player.changespeed(0,3)
                if wall_collision:
                    player.changespeed(0,-3)
     
            elif event.key == pygame.K_f:
                start = True
                roar.play()
                for x in range(1):
                    fire1 = Fireball()
                    fire2 = Fireball()
                    fire3 = Fireball()
                    fire4 = Fireball()
                    fire5 = Fireball()
                    all_sprite_list.add(fire1)
                    fire_list.add(fire1)
                    all_sprite_list.add(fire2)
                    fire_list.add(fire2)
                    all_sprite_list.add(fire3)
                    fire_list.add(fire3)
                    all_sprite_list.add(fire4)
                    fire_list.add(fire4)
                    all_sprite_list.add(fire5)
                    fire_list.add(fire5)
                    whoosh.play()
            elif event.key == pygame.K_e:
                shield = Shield()
                all_sprite_list.add(shield)
                shield_list.add(shield)
                held = True

                #Frogger
        elif event.type == pygame.KEYUP:
            #Frogger
            if event.key == pygame.K_LEFT:
                #Frogger
                player.changespeed(3,0)
                if wall_collision:
                    player.changespeed(0,0)
  
                #Frogger
            elif event.key == pygame.K_RIGHT:
                #Frogger
                player.changespeed(-3,0)
                if wall_collision:
                    player.changespeed(0,0)
      
                #Frogger
            elif event.key == pygame.K_UP:
                #Frogger
                player.changespeed(0,3)
                if wall_collision:
                    player.changespeed(0,0)

                #Frogger
            elif event.key ==pygame.K_DOWN:
                #Frogger
                player.changespeed(0,-3)
                if wall_collision:
                    player.changespeed(0,0)
            elif event.key ==pygame.K_e:
                all_sprite_list.remove(shield)
                shield_list.remove(shield)
                held = False
                timershield = 0
       

            
 
    # --- Game logic should go here

    shield_list.update()

    fire_list.update()
    if attack != True and start == True:
        if player.rect.x >225 and player.rect.x <250 or player.rect.x >475 and player.rect.x <500:
                num = random.randrange(75)
                print(num)
                if num == 27:
                    print("potato")
                    attack = True
    
    num2 = random.randrange(15)
    if breathed == False and timer != 100 and start == True:
        if num2 == 5:
            timer += 1
            print(timer)

    if attack == True and timer == 100:
        all_sprite_list.add(breath)
        breath_list.add(breath)
        breathed = True
        if breathed == True:
            num3 = random.randrange(15)
            if num3 ==10:
                timer2 +=1
                print("toe")
                if timer2 ==25:
                    print("cat")
                    attack = False
                    timer = 0
                    timer2 = 0
                    all_sprite_list.remove(breath)
                    breath_list.remove(breath)
                    breathed = False
                    print("popsicle")


    if held == True:
        num4 = random.randrange(15)
        if num4 == 9:
            timershield += 1
            print("onion")
            if timershield == 10:
                all_sprite_list.remove(shield)
                shield_list.remove(shield)
                timershield = 0
                            
  


    your_dead = pygame.sprite.spritecollide(player, fire_list, False)

    you_win = pygame.sprite.spritecollide(player, dragon_list, False)

    blocked = pygame.sprite.groupcollide(fire_list, wall_list, True, False)

    coin_gathered = pygame.sprite.spritecollide(player, coin_list, True)

    wall_collision = pygame.sprite.spritecollide(player, wall_list, False)

    hit_breath = pygame.sprite.spritecollide(player, breath_list, False)

    defended = pygame.sprite.groupcollide(shield_list, fire_list, False, True)

    

    

    for x in coin_gathered:
        score += 1
        print("Coin")
    for i in blocked:
        
        fire = Fireball()
        all_sprite_list.add(fire)
        fire_list.add(fire)
        whoosh.play()

    for i in defended:

        fire = Fireball()
        all_sprite_list.add(fire)
        fire_list.add(fire)
        whoosh.play()

    for i in hit_breath:
        killed += 1
        dead = True
        print("breath")
        whoosh.play()
        roar.play()

    for x in your_dead:
        killed += 1
        print(killed)
        dead = True
        print("fire")
        roar.play()
        whoosh.play()

    for x in you_win:
        win = True
        print("rat")
        roar.play()


    all_sprite_list.update()
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    
    # --- Drawing code should go here
    screen.blit(bg, [0,0])

    

    


    if start != True:
        fontinstruction = pygame.font.SysFont("Arial", 35, True, False)
        render_fontinstruct = fontinstruction.render("You must get to the dragon to slay it to win", True, RED)
        render_fontinstruct2 = fontinstruction.render("get past the obstacles and save the princess", True, RED)
        render_fontinstruct4 = fontinstruction.render("Hold e to use your shield to block the fireballs", True, RED)
        render_fontinstruct5 = fontinstruction.render("Be careful, it won't block the dragon's breath", True, RED)
        render_fontinstruct6 = fontinstruction.render("The king has requested his treasure as well", True, RED)
        render_fontinstruct3 = fontinstruction.render("F to start!", True, RED)
        screen.blit(render_fontinstruct, [50,100])
        screen.blit(render_fontinstruct2, [50,150])
        screen.blit(render_fontinstruct3, [50,350])
        screen.blit(render_fontinstruct4, [50,200])
        screen.blit(render_fontinstruct5, [50,250])
        screen.blit(render_fontinstruct6, [50,300])
    
    elif start == True:
        if dead != True:
            all_sprite_list.draw(screen)
            fonthealth = pygame.font.SysFont("Arial", 25, True, False)
            render_font = fonthealth.render("Score: " + str(score), True, WHITE)
            screen.blit(render_font, [50, 25])
        elif dead != False:
            all_sprite_list.empty()
            screen.fill(BLACK)
            fontdie = pygame.font.SysFont("Arial", 100, True, False)
            fontdie2 = pygame.font.SysFont("Arial", 45, True, False)
            rendered_fontdie = fontdie.render("You Lost!", True, RED)
            rendered_fontdie1 = fontdie2.render("You failed to save the princess.", True, RED)
            rendered_fontdie2 = fontdie2.render("You had a score of: " + str(score) + "!", True, RED)
            screen.blit(rendered_fontdie, [150,100])
            screen.blit(rendered_fontdie1, [50,200])
            screen.blit(rendered_fontdie2, [150,300])
        if win == True:
            all_sprite_list.empty()
            screen.fill(BLACK)
            fontwin = pygame.font.SysFont("Arial", 45, True, False)
            rendered_fontwin = fontwin.render("You Slayed The Dragon", True, RED)
            rendered_fontwin2 = fontwin.render("&", True, RED)
            rendered_fontwin3 = fontwin.render("Saved The Princess!", True, RED)
            rendered_fontwin4 = fontwin.render("You have a score of: " + str(score) + "!", True, RED)
            rendered_fontwin5 = fonthealth.render("You collected all of the King's treasure!", True, RED)
            screen.blit(princess, [50,150])
            screen.blit(rendered_fontwin, [150,100])
            screen.blit(rendered_fontwin2, [150,150])
            screen.blit(rendered_fontwin3, [150,200])
            screen.blit(rendered_fontwin4, [150,300])
            if score == 11:
                screen.blit(rendered_fontwin5, [150,350])
            


        
                                       
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
