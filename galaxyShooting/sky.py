import pygame
import random
import math

# initializing all imported pygame module rather initialize individual module
pygame.init()

# creating the window
width = 800
height = 600
win = pygame.display.set_mode((width, height))

# background, logo, Title
background = pygame.image.load('assets/images/back.jpg')
pygame.display.set_caption("Guardian of the Galaxy")
icon = pygame.image.load('assets/images/aircraft.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('assets/images/jet.png')
playerx = 370
playery = 480
playerx_change = 0

# enemy
enemyimg = pygame.image.load('assets/images/enemy.png')
enemyx = random.randint(0, 735)
enemyy = random.randint(-10, -5)
enemyy_change = 0.5

#  bullet
bulletimg = pygame.image.load('assets/images/bullet (1).png')
bulletx = 370
bullety = 480
bullety_change = 1
mode = "on"

# score
score = 0
s_text = pygame.font.Font('assets/fonts/dominojackexpandital.ttf', 40)


def scoretext():
    text = s_text.render("Score = " + str(score), True, (255, 255, 255))
    win.blit(text, (8, 8))


# game over
over_font = pygame.font.Font('freesansbold.ttf', 64)
a = 0


def game_over():
    game_over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    win.blit(game_over_text, (200, 250))




def player(x, y):
    win.blit(playerimg, (x, y))


def enemy(x, y):
    win.blit(enemyimg, (x, y))


def shoot(x, y):
    global mode
    mode = "off"
    win.blit(bulletimg, (x + 20, y))


def isCollision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt(math.pow(enemyx - bulletx, 2) + (math.pow(enemyy - bullety, 2)))
    if distance <= 29:
        return True
    else:
        return False


def player_Enemy_Collision(enemyx, enemyy, playerx, playery):
    distance = math.sqrt(math.pow(enemyx - playerx, 2) + (math.pow(enemyy - playery, 2)))
    if distance <= 50:
        return True
    else:
        return False


# mainLoop
end = True
while end:

    win.blit(background, (0, 0))

    # EXIT button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerx_change = 1
            if event.key == pygame.K_LEFT:
                playerx_change = -1

            if event.key == pygame.K_UP:
                if mode == "on":
                    bulletx = playerx
                    shoot(bulletx, bullety)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerx_change = 0

    # Collision
    collision = isCollision(enemyx, enemyy, bulletx, bullety)
    if collision:
        score += 1
        bullety = 480
        mode = "on"
        enemyx = random.randint(0, 735)
        enemyy = random.randint(-10, -5)

    p_E_Collision = player_Enemy_Collision(enemyx, enemyy, playerx, playery)
    if p_E_Collision:
        i = 0
        while i < 100:
            game_over()
            score = 0
            i += 1
        if enemyy >= 500:
            #break
            #end = False
            score = 0
            bullety = 480
            mode = "on"
            enemyx = random.randint(0, 735)
            enemyy = random.randint(-10, -5)




    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 735:
        playerx = 735

    if bullety <= 0:
        bullety = 480
        mode = "on"

    if mode == "off":
        shoot(bulletx, bullety)
        bullety -= bullety_change

    enemyy += enemyy_change

    if enemyy >= 565:
        bullety = playery
        mode = "on"
        enemyx = random.randint(0, 735)
        enemyy = random.randint(-10, -5)

    player(playerx, playery)
    enemy(enemyx, enemyy)
    scoretext()
    pygame.display.update()
