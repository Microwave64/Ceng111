import pygame
import random
import math
from pygame import mixer


pygame.init()
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((800,600))

# Background
#background = pygame.image.load("baby_dino.png")

# Background sound
mixer.music.load('Life is a Highway.wav')
mixer.music.play(-1)
 
#caption and icon
pygame.display.set_caption("Dragon Hunter")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)


# Player
player_image = pygame.image.load('ninja.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


# Enemy:
enemy_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5


for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load('final-boss.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(random.uniform(-0.13,0.18))
    enemyY_change.append(random.uniform(0.13,0.18))


# Bullet

# Ready -> bullet can't be seen on the screen
# Fire -> bullet can be seen on the screen
bullet_image = pygame.image.load('ninja-blade.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.42
bullet_state = "ready"



# Game Over
finish_font = pygame.font.Font("freesansbold.ttf",64)
reload_font = pygame.font.Font("freesansbold.ttf",16)



# Score_board .render is used to write the value cause after that blint will be used.
score_value = 0    
font = pygame.font.Font('freesansbold.ttf',32)   #Free font in pygame   
testX = 10
testY = 10




# FUNCTIONS

# Start position of object and movement of it
def player(x,y):
    screen.blit(player_image,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_image[i],(x[i],y[i]))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_image,(x+16,y+10))

def is_collision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 31 and bullet_state == "fire":
        return True
    else:
        return False

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (0,0,0))
    screen.blit(score,(x,y))


def is_dead(enemyX,enemyY,playerX,playerY):
    dist = math.sqrt(math.pow(enemyX - playerX,2)+math.pow(enemyY - playerY,2))
    if dist < 48:
        return True
    else:
        return False

    
def game_over():
    finish = finish_font.render("GAME OVER" , True, (0,0,0))
    replay = reload_font.render("press shit to play again", True, (0,0,0))
    screen.blit(finish,(225,250))
    screen.blit(replay,(320,330))

def create_enemy():
    enemy_image.append(pygame.image.load('final-boss.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(random.uniform(-0.13,0.18))
    enemyY_change.append(random.uniform(0.13,0.18))
    global num_of_enemies
    num_of_enemies += 1


# Necessary Flags
dead_body = False
slience = True
constant = 1


# Loop
running = True
while running:
    screen.fill((255,158,63))
    #screen.blit(background,(-150,-50))
    if dead_body and slience:
        slience = False        
        mixer.music.load('Short clip COFFIN DANCE.wav')
        mixer.music.play(-1)
    
    
    for event in pygame.event.get():
        if dead_body:
            playerX_change = 0
            playerY_change = 0
        if event.type == pygame.QUIT:
            running = False
        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # This doesn't work I know but I still want to try to close with this way
                # The right way is just use quit function
                # Actualy it closes the file just because the error! 
                try: 
                    File = "Hello_game.py"
                    File.close()
                except AttributeError:
                        quit()
            
            # Restart the game
            if dead_body and event.key == pygame.K_LSHIFT:
                dead_body = False
                score_value = 0 
                slience = True
                constant = 1

                playerX = 370
                playerY = 480
                playerX_change = 0
                playerY_change = 0

                bullet_image = pygame.image.load('ninja-blade.png')
                bulletX = 0
                bulletY = 480
                bulletX_change = 0
                bulletY_change = 0.3
                bullet_state = "ready"

                enemy_image = []
                enemyX = []
                enemyY = []
                enemyX_change = []
                enemyY_change = []
                num_of_enemies = 5

                for i in range(num_of_enemies):
                    enemy_image.append(pygame.image.load('final-boss.png'))
                    enemyX.append(random.randint(0,735))
                    enemyY.append(random.randint(50,150))
                    enemyX_change.append(random.uniform(-0.18,0.18))
                    enemyY_change.append(random.uniform(0.13,0.18))

                mixer.music.unload()
                mixer.music.load('Life is a Highway.wav')
                mixer.music.play(-1)
 

        if event.type == pygame.KEYDOWN and not dead_body:
            if event.key == pygame.K_LEFT:
                playerX_change = - 0.35 * constant 
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.35 * constant
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('Katana Swing Cut - Sound Effect for editing.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    bulletY = playerY
                    bulletX_change = playerX_change * 0.37
                    fire_bullet(playerX,playerX)
            if event.key == pygame.K_UP:
                playerY_change = -0.35 * constant 
            if event.key == pygame.K_DOWN:
                playerY_change = 0.35 * constant    
        if event.type == pygame.KEYUP and not dead_body:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0


    # Player movement
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: #800-64pixel = 736 
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    

    # Enemy Movement
    for i in range(num_of_enemies):
        dead = is_dead(enemyX[i],enemyY[i],playerX,playerY)
        if dead:
            dead_body = True
            for j in range(num_of_enemies):
                enemyX_change[j] = 0
                enemyY_change[j] = 0 
            game_over()

        
                
        enemyX[i] += enemyX_change[i]
        enemyY[i] += enemyY_change[i]
        
        if enemyX[i] <= 0:
            enemyX_change[i] = random.uniform(0.1,0.15)
        elif enemyX[i] >= 736: #800-64pixel = 736 
            enemyX_change[i] = random.uniform(-0.15,0.1)

        if enemyY[i] <= 0:
            enemyY_change[i] = random.uniform(0.1,0.15)
        elif enemyY[i] >= 536:
            enemyY_change[i] = random.uniform(-0.1,-0.15)
     
        # Collision (in the former for loop)
        collision = is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            kill_sound = mixer.Sound("Fireball_sound.wav")
            kill_sound.play()
            bulletY = 480 
            bullet_state = "ready"
            score_value += 1
            if score_value % 10 == 0:
                constant *= 1.3
                create_enemy()
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
            enemyX_change[i] = random.uniform(-0.15,0.15)
            enemyY_change[i] = random.uniform(0.1,0.15)
        enemy(enemyX,enemyY,i)

    

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        if not dead_body:
            bulletY -= bulletY_change * constant
            bulletX += bulletX_change * constant


    player(playerX,playerY)
    enemy(enemyX,enemyY,i)
    show_score(testX,testY)
    if dead_body:
        game_over()
    

    pygame.display.update()


