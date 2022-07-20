import pygame

from pygame.locals import *

pygame.init()

running = True
screen = pygame.display.set_mode((800, 800))

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()
