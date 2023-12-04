from sys import exit

import pygame


def set_size_font(size):
    return pygame.font.Font('font/Pixeltype.ttf', size)


def display_score():
    cur_time = int(pygame.time.get_ticks() / 1000) - start_time
    text_font = set_size_font(50)
    score_surface = text_font.render(f'Score: {cur_time} ', False, 'Black')
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)


def game_over_screen(final_score):
    screen.fill((94, 129, 162))

    text_font = set_size_font(50)
    final_score_sur = text_font.render(f'Your Score:{final_score}', False, (111, 196, 169))
    final_score_rect = final_score_sur.get_rect(center=(400, 300))

    screen.blit(player_stand, player_stand_rect)
    screen.blit(game_over_surface, game_over_rect)
    screen.blit(final_score_sur, final_score_rect)
    screen.blit(game_restart_surface, game_restart_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
start_time = 0
"""define static object game"""
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

"""define dynamic object """
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft=(800, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(100, 300))
"""define game over screen"""
text_font = set_size_font(80)
game_over_surface = text_font.render('GAME OVER', False, (111, 196, 169))
game_over_rect = game_over_surface.get_rect(center=(400, 50))

player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400, 200))

text_font = set_size_font(30)
game_restart_surface = text_font.render('To  Restart  Press  Enter ', False, (111, 196, 169))
game_restart_rect = game_restart_surface.get_rect(center=(400, 350))

player_gravity = 0
game_active = True
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
                game_active = True
                snail_rect.left = 800
                # player_rect.right = -10
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        """define position on the game board"""
        screen.blit(sky_surface, (0, 0))
        screen.blit(snail_surface, snail_rect)
        screen.blit(ground_surface, (0, 300))
        # pygame.draw.rect(screen, '#c0e8ec', score_rect, 6, border_radius=10)
        display_score()

        """define the moving object on game board"""
        """snail:"""
        if snail_rect.right > 0:
            snail_rect.left -= 10
        else:
            snail_rect.left = 800

        """player:"""
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # if player_rect.left < 800:
        #     player_rect.right += 3
        # else:
        #     player_rect.right = 10

        if player_rect.colliderect(snail_rect):
            game_active = False
            final_score = int(pygame.time.get_ticks() / 1000) - start_time
    else:
        game_over_screen(final_score)

    pygame.display.update()
    clock.tick(60)
