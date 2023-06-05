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
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
text_surface = test_font.render('My Game', False, 'Black') # text info, anti-alias, color

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # draw all our elements
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    # screen.blit(snail_surface, (snail_x_pos, 250))
    snail_x_pos -= 4
    # if snail_x_pos < -100:
    #     snail_x_pos = 800
    # player_rect.left += 1
    # print(player_rect.left) # at position 48
    snail_rect.x -= 4 # snail moves left
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)
    # update everything
    pygame.display.update()
    clock.tick(60) # should not run faster than 60 frames per second in the while true loop
