from sys import exit

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = text_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(800, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png')
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    screen.blit(snail_surface, snail_rect)
    if snail_rect.right > 0:
        snail_rect.left -= 4
    else:
        snail_rect.left = 800
    screen.blit(player_surf, player_rect)
    if player_rect.left < 800:
        player_rect.right += 4
    else:
        player_rect.right = -100
    pygame.display.update()
    clock.tick(60)
