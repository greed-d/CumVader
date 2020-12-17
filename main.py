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
playerImg = pygame.image.load("./penis.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0

# Show enemy
enemyImg = pygame.image.load("./ass.png")
enemyImg = pygame.transform.scale(enemyImg, (128, 128))
enemyX = randint(0, 800)
enemyY = randint(50, 150)
enemyX_change = 1.5
enemyY_change = 15

# Show Bullet
# Ready = You can't see the bullet
# Fire = The bullet is moving
bulletImg = pygame.image.load("./cumBullet.png")
bulletImg = pygame.transform.scale(bulletImg, (32, 32))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 7
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def bulletFire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Main loop
def mainLoop():
    global screen
    global playerX, playerY, playerX_change
    global enemyX, enemyY, enemyX_change, enemyY_change
    global bulletY, bulletY_change

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

                if event.key == pygame.K_SPACE:
                    bulletFire(playerX, playerY)

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

        if bullet_state is "fire":
            bulletFire(playerX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        enemy(enemyX, enemyY)
        pygame.display.update()


mainLoop()