import pygame
import random
import math

from pygame import mixer
pygame.init()
mixer.init()
gamescreen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("Particle Accelerator")
clock = pygame.time.Clock()
quack = pygame.mixer.Sound('quack.mp3')

gameOver = False

xpos = []  # position
ypos = []
xVel = []
yVel = []  # velocity
sizes = []
ticker = []
speed = 15

rock = pygame.image.load('Rock.png')
rock = pygame.transform.scale(rock, (100, 100))

while not gameOver:
    pygame.mixer.Sound.play(quack)
    clock.tick(60)

    # particles
    for i in range(1):
        if len(xpos) < 1000:
            # random vel
            velX = random.uniform(-1, 1)
            velY = random.uniform(-1, 1)

            # magnitude of velocity vector
            magnitude = math.sqrt(velX**2 + velY**2)

            if magnitude != 0:
                normalizedVelX = speed * velX / magnitude
                normalizedVelY = speed * velY / magnitude
            else:
                normalizedVelX = 0
                normalizedVelY = 0

            xpos.append(450)
            ypos.append(450)
            sizes.append(1)
            # ticker.append(0)
            xVel.append(normalizedVelX)
            yVel.append(normalizedVelY)

    # Event Handle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    # physics
    for i in range(len(xpos)):

        # update pos
        xpos[i] += xVel[i]
        ypos[i] += yVel[i]
        sizes[i] = sizes[i] + .03

        # boundary check
        if xpos[i] < 0 or xpos[i] > 900 or ypos[i] < 0 or ypos[i] > 900:
            xpos[i] = 450
            ypos[i] = 450
            sizes[i] = 1

            velX = random.uniform(-1, 1)
            velY = random.uniform(-1, 1)

            magnitude = math.sqrt(velX**2 + velY**2)

            if magnitude != 0:
                xVel[i] = speed * velX / magnitude
                yVel[i] = speed * velY / magnitude
            else:
                xVel = 0
                yVel = 0

    # render
    gamescreen.fill((0, 0, 0))
    for i in range(len(xpos)):
        gamescreen.blit(rock, (int(xpos[i]), int(ypos[i])))

        pygame.draw.circle(gamescreen, ((random.randrange(0, 255), random.randrange(
            0, 255), random.randrange(0, 255))), (int(xpos[i]), int(ypos[i])), int(sizes[i]))
    pygame.display.flip()

# end of game
pygame.quit()
