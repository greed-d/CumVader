import pygame
from random import randint

# Initialize pygame
pygame.init()

# Displaying the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Show Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load("./spaceship.png")
pygame.display.set_icon(icon)

# Show background
background = pygame.image.load("./background.jpg")

# Show player
playerImg = pygame.image.load("./spaceship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Show enemy
enemyImg = pygame.image.load("./alien.png")
enemyX = randint(0, 800)
enemyY = randint(50, 150)
enemyX_change = 3
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Main loop
def mainLoop():
    global screen
    global playerX
    global playerY
    global playerX_change
    global enemyX
    global enemyY
    global enemyX_change
    global enemyY_change

    running = True
    while running:
        screen.fill((79, 5, 252, 0.849))

        # Background Image
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # To see if the key is pressed and released
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5

                if event.key == pygame.K_RIGHT:
                    playerX_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        enemyX += enemyX_change

        if enemyX <= 0:
            enemyX_change = 3
            enemyY += enemyY_change
        elif enemyX >= 736:
            enemyX_change = -3
            enemyY += enemyY_change

        # if enemyX <= 0:
        #     enemyY_change = 0.3
        # elif enemyX >= 736:
        #     enemyY_change = 0.3

        player(playerX, playerY)
        enemy(enemyX, enemyY)
        pygame.display.update()


mainLoop()