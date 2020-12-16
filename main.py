import pygame

#Initialize pygame
pygame.init()

#Displaying the screen
width = 800
height = 600 
screen = pygame.display.set_mode((width, height))

#Show Icon 
pygame.display.set_caption('Chess')
icon = pygame.image.load('./chess.png')
pygame.display.set_icon(icon)

#Show player
playerImg = pygame.image.load('./spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

#Main loop
def mainLoop():
    global screen 
    global playerX
    global playerY
    global playerX_change
    

    running = True
    while running:
        screen.fill((192, 246, 248, 0.849))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.3

                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736

        playerX += playerX_change
        player(playerX, playerY)
        pygame.display.update() 

mainLoop()