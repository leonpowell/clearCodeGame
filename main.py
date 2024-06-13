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
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface =  test_font.render('My game', False, 'Purple')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(topleft = (80,215))
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # draw all out elements and update everything

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface, (snail_x_pos,270))
    screen.blit(player_surf, player_rect)
    pygame.display.update()
    clock.tick(FPS)