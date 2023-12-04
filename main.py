from random import randint
from sys import exit

import pygame


def set_size_font(size):
    return pygame.font.Font('font/Pixeltype.ttf', size)


def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= 2:
            player_index = 0
        player_surf = player_walk[int(player_index)]


def open_screen():
    screen.fill((94, 129, 162))
    screen.blit(pixel_surface, pixel_rect)
    screen.blit(player_stand, player_stand_rect)
    screen.blit(game_restart_surface, game_restart_rect)


def display_score():
    cur_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = set_size_font(50).render(f'Score: {cur_time} ', False, 'Black')
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)
    return cur_time


def game_over_screen(final_score):
    screen.fill((94, 129, 162))

    final_score_sur = set_size_font(50).render(f'Your Score:{final_score}', False, (111, 196, 169))
    final_score_rect = final_score_sur.get_rect(center=(400, 310))

    screen.blit(player_stand, player_stand_rect)
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(final_score_sur, final_score_rect)
    screen.blit(game_restart_surface, game_restart_rect)


def obstacle_movement(obstacle_rect_list):
    if obstacle_rect_list:
        for obstacle_rect in obstacle_rect_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        return [obstacle for obstacle in obstacle_rect_list if obstacle.right > 0]

    else:
        return []


def collisions(player, obstacle_list):
    for obstacle in obstacle_list:
        if player.colliderect(obstacle):
            return True
        return False


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
player_gravity = 0
game_active = False
start_time = 0
score = 0
"""define static object game"""
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

pixel_surface = set_size_font(80).render('Pixel runner', False, (111, 196, 169))
pixel_rect = pixel_surface.get_rect(center=(400, 50))

"""define dynamic object """
"""snail animation"""
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_index = 0
snail_surf = snail_frames[snail_index]
"""fly animation"""
fly_frame_1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly_frame_2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_index = 0
fly_surf = fly_frames[fly_index]
"""obstacle animation"""
obstacle_rect_list = []

"""player animation"""
player_walk_1 = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(100, 300))
player_jump = pygame.image.load('graphics/Player/jump.png').convert_alpha()
"""define game over screen"""
game_over_surface = set_size_font(80).render('GAME OVER', False, (111, 196, 169))
game_over_rect = game_over_surface.get_rect(center=(400, 50))

player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400, 180))

game_restart_surface = set_size_font(30).render('Press  Enter To Run', False, (111, 196, 169))
game_restart_rect = game_restart_surface.get_rect(center=(400, 350))
"""define timer """
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1400)

snail_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_timer, 500)

fly_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_timer, 100)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if player_rect.bottom == 300:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos):
                        player_gravity = -20
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player_gravity = -20
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                obstacle_rect_list = []
                player_rect.bottom = 300
                player_gravity = 0
                game_active = True

                start_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomleft=(randint(800, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomleft=(randint(800, 1100), 200)))

            if event.type == snail_timer:
                if snail_index == 0:
                    snail_index = 1
                else:
                    snail_index = 0
                snail_surf = snail_frames[snail_index]

            if event.type == fly_timer:
                if fly_index == 0:
                    fly_index = 1
                else:
                    fly_index = 0
                fly_surf = fly_frames[fly_index]

    if game_active:
        """define position on the game board"""
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        """define the moving object on game board"""

        """player:"""
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        "obstacle:"
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        if collisions(player_rect, obstacle_rect_list):
            game_active = False

    else:
        if score == 0:
            open_screen()
        else:
            game_over_screen(score)

    pygame.display.update()
    clock.tick(60)
