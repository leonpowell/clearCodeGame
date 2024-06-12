import pygame
from sys import exit
pygame.init()


# settings
width = 800
height = 400
FPS = 60


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all out elements and update everything

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0, 300))
    pygame.display.update()
    clock.tick(FPS)