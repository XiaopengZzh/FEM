import pygame

import utils
from utils import screen_projection

import solver
import odes

dt = 0.01
recordInterval = 10
# stepFunc = solver.oneTimestep_FEuler
stepFunc = solver.oneTimestep_RK4

x = odes.initUnitCircle()
xT = odes.initUnitCircle()
numSeg = 100
uCircle = utils.generateUnitCircle(numSeg)


running = True
timestep = 0
pygame.init()
screen = pygame.display.set_mode(utils.resolution)

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.circle(screen, (0, 0, 255), screen_projection(x), 10)
    pygame.draw.circle(screen, (255, 0, 0), screen_projection(xT), 10)
    for i in range(numSeg):
        pygame.draw.aaline(screen, (0, 255, 0), screen_projection(uCircle[i]), screen_projection(uCircle[(i + 1) % numSeg]))
    pygame.display.flip()

    timestep += 1
    x = stepFunc(x, dt, odes.fUnitCircle)
    xT = odes.exactSolutionUnitCircle(timestep * dt)

    pygame.time.wait(int(dt * 1000))

pygame.quit()