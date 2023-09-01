import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640,480))

pygame.display.set_caption('第一个游戏')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((123,123,123))
    pygame.display.update()