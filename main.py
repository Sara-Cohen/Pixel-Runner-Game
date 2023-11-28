from sys import exit

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('Blue')

test_surface2 = pygame.Surface((10, 20))
test_surface2.fill('Green')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface, (200, 100))
    screen.blit(test_surface2,(100,50))

    pygame.display.update()
    clock.tick(60)
