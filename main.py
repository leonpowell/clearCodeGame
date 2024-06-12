import pygame
from sys import exit
pygame.init()


# settings
width = 800
height = 600
FPS = 60


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100,100))
test_surface.fill('Purple')
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all out elements and update everything

    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(FPS)