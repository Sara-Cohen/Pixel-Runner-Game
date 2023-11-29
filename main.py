from sys import exit
import pygame



pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
"""define static object game"""
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

text_font_30 = pygame.font.Font('font/Pixeltype.ttf', 30)
text_font_50 = pygame.font.Font('font/Pixeltype.ttf', 50)
text_font_70 = pygame.font.Font('font/Pixeltype.ttf', 70)
score=0
score_surface = text_font_50.render(f'Score: {score} ', False, 'Black')
score_rect = score_surface.get_rect(center=(400, 50))

game_over_surface = text_font_70.render('GAME OVER', False, 'White')
game_over_rect = game_over_surface.get_rect(center=(400, 200))

game_restart_surface=text_font_30.render('To  Restart  Press  Enter ',False,'Gold')
game_restart_rect=game_restart_surface.get_rect(center=(400, 280))
"""define dynamic object """
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft=(800, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png')
player_rect = player_surf.get_rect(midbottom=(80, 300))
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
                player_rect.right = -10

    if game_active:
        """define position on the game board"""
        screen.blit(sky_surface, (0, 0))
        screen.blit(snail_surface, snail_rect)
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 6, border_radius=10)
        screen.blit(score_surface, score_rect)

        """define the moving object on game board"""
        """snail:"""
        if snail_rect.right > 0:
            snail_rect.left -= 4
        else:
            snail_rect.left = 800

        """player:"""
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if player_rect.left < 800:
            player_rect.right += 1
        else:
            player_rect.right = -100
        if player_rect.colliderect(snail_rect):
            game_active = False
    else:
        screen.fill('Black')

        screen.blit(game_over_surface, game_over_rect)
        screen.blit(game_restart_surface,game_restart_rect)
    pygame.display.update()
    clock.tick(60)
