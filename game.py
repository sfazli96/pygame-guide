import pygame
from sys import exit

pygame.init()
# display surface
screen = pygame.display.set_mode((800, 400)) # width, height
# update the title
pygame.display.set_caption('Runner')
# clock object helps with time and controlling the framerate
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,200)) # width, height
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all our elements
    screen.blit(test_surface, (0, 0))
    # update everything
    pygame.display.update()
    clock.tick(60) # should not run faster than 60 frames per second in the while true loop
