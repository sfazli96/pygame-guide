import pygame
from sys import exit
from random import randint

# display the score
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64, 64, 64)) # create a new score rectangle surface
    score_rect = score_surface.get_rect(center = (400, 50)) # create the rectangle
    screen.blit(score_surface, score_rect) # now blit/show it
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)

        # list comprehension
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

pygame.init()
# display surface
screen = pygame.display.set_mode((800, 400)) # width, height
# update the title
pygame.display.set_caption('Runner')
# clock object helps with time and controlling the framerate
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50) # font type, font size
game_active = False
start_time = 0
score = 0

# test_surface = pygame.Surface((100,200)) # width, height
# test_surface.fill('Red')
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
# score_surface = test_font.render('My Game', False, (64, 64, 64)) # text info, anti-alias, color
# score_rect = score_surface.get_rect(center = (400, 50))

# loading the snail surface
# obstacle logic
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# snail_rect = snail_surface.get_rect(bottomright = (600, 300))

fly_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

# Loading the player walk surface
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80, 300))
player_gravity = 0

# Intro Screen
player_stand = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# Title from intro screen
game_name = test_font.render('Pixel Runner', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center = (400, 80))

# game message of press space to run
game_message = test_font.render('Press space to run', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300: # only ALLOWS jump if player is on ground
                    player_gravity = -20 # player jumps now up when user clicks on player
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300: # only ALLOWS jump if player is on ground
                    player_gravity = -20 # player jumps now up only when user presses spacebar input keyboard
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 210)))
    if game_active: # actual game, part of the game
        # draw all our elements
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        # draw the rectangles, ellipses, etc
        # pygame.draw.rect(screen, '#c0e8ec', score_rect) # 3 arguments display screen, color and score
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # screen.blit(score_surface, score_rect)
        score = display_score()

        # snail_rect.x -= 4 # snail moves left
        # if snail_rect.right <= 0:
        #     snail_rect.left = 800
        # screen.blit(snail_surface, snail_rect)

        # Player Jumping/Gravity
        player_gravity += 1 # want to move the player's gravity downwards
        player_rect.y += player_gravity
        if player_rect.bottom >= 300: # creating the player rect bottom floor
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision
        game_active = collisions(player_rect, obstacle_rect_list)

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

        # collision for game
    else: # some kind of intro/menu screen
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear() # remove every item
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    # update everything
    pygame.display.update()
    clock.tick(60) # should not run faster than 60 frames per second in the while true loop
