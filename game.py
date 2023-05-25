import pygame
from sys import exit

pygame.init()
# display surface
screen = pygame.display.set_mode((800, 400)) # width, height

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all our elements
    # update everything
    pygame.display.update()
