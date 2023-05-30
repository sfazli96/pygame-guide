import pygame
from sys import exit

pygame.init()
# display surface
screen = pygame.display.set_mode((800, 400)) # width, height
# update the title
pygame.display.set_caption('Runner')
# clock object helps with time and controlling the framerate
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) # font type, font size

# test_surface = pygame.Surface((100,200)) # width, height
# test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/sky.jpg')
ground_surface = pygame.image.load('graphics/ground.jpg')
text_surface = test_font.render('My Game', False, 'Black') # text info, anti-alias, color

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all our elements
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 250))
    screen.blit(text_surface, (300, 50))
    # update everything
    pygame.display.update()
    clock.tick(60) # should not run faster than 60 frames per second in the while true loop
