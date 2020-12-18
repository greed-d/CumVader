import pygame
from random import randint
import math
import time

# Initialize pygame
pygame.init()

# Displaying the screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Show Icon
pygame.display.set_caption("CumVaders")
icon = pygame.image.load("./images/ass1.png")
pygame.display.set_icon(icon)

# Show background
background = pygame.image.load("./images/background.jpg")

# Show player
playerImg = pygame.image.load("./images/penis.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 3

# Show enemy
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("./images/ass1.png"))
    enemyX.append(randint(0, 729))
    enemyY.append(randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(15)

# Show Bullet
# Ready = You can't see the bullet
# Fire = The bullet is moving
bulletImg = pygame.image.load("./images/cumBullet.png")
bulletImg = pygame.transform.scale(bulletImg, (32, 32))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5.75
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font("./Fonts/Poppins-Bold.ttf", 32)

textX = 10
textY = 10

# Game over text font
overFont = pygame.font.Font("./Fonts/Poppins-Bold.ttf", 32)


def showScore(x, y):
    score = font.render("Score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def gameOver():
    overText = overFont.render("YOU WASTED PRECIOUS CUM FUCKER", True, (255, 255, 255))
    screen.blit(overText, (130, 250))
    print("this is a test")
    time.sleep(1)


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def bulletFire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(
        (math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    )
    if distance < 27:
        return True
    else:
        return False


# Main loop
def mainLoop():
    global screen
    global playerX, playerY, playerX_change
    global enemyX, enemyY, enemyX_change, enemyY_change
    global bulletY, bulletY_change, bullet_state, bulletX
    global score_value

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
                    if bullet_state is "ready":
                        bulletX = playerX
                        bulletFire(bulletX, playerY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        elif playerX >= 729:
            playerX = 729

        # if enemyY[i] > 180:
        #     gameOver()
        #     for j in range(num_of_enemies):
        #         enemyY[j] = 2000

        for i in range(num_of_enemies):

            if enemyY[i] > 190:
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                gameOver()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 2
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 729:
                enemyX_change[i] = -2
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                collisionSound = pygame.mixer.Sound("./sound/collision.wav")
                collisionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                # print(score_value)
                enemyX[i] = randint(0, 729)
                enemyY[i] = randint(50, 150)

            enemy(enemyX[i], enemyY[i], i)

        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            bulletFire(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        showScore(textX, textY)
        pygame.display.update()


mainLoop()