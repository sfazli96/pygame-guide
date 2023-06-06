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
score_surface = test_font.render('My Game', False, (64, 64, 64)) # text info, anti-alias, color
score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: # only ALLOWS jump if player is on ground 
                player_gravity = -20 # player jumps now up when user clicks on player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 300: # only ALLOWS jump if player is on ground
                player_gravity = -20 # player jumps now up only when user presses spacebar input keyboard

    # draw all our elements
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # draw the rectangles, ellipses, etc
    pygame.draw.rect(screen, '#c0e8ec', score_rect) # 3 arguments display screen, color and score
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
    # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))

    screen.blit(score_surface, score_rect)
    snail_rect.x -= 4 # snail moves left
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    # Player Jumping/Gravity
    player_gravity += 1 # want to move the player's gravity downwards
    player_rect.y += player_gravity
    if player_rect.bottom >= 300: # creating the player rect bottom floor
        player_rect.bottom = 300

    screen.blit(player_surf, player_rect)

    # Keyboard input
    # print(pygame.key.get_pressed())
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')

    # print(player_rect.colliderect(snail_rect))
    # if player_rect.colliderect(snail_rect): # basic version of collision
    #     print("collision")

    # mouse_pos = pygame.mouse.get_pos() # get the position of the mouse
    # if player_rect.collidepoint(mouse_pos):
    #     # print('Collision')
    #     print(pygame.mouse.get_pressed())

    # update everything
    pygame.display.update()
    clock.tick(60) # should not run faster than 60 frames per second in the while true loop
