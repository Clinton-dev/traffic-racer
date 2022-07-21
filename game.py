import pygame
import random

from pygame.locals import *

size = height, width =(800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1


pygame.init()

running = True
screen = pygame.display.set_mode(size)
screen.fill((60, 220, 0))

pygame.display.update()

# user vehicle
car = pygame.image.load('car.png')
car_loc = car.get_rect()
car_loc.center = right_lane, height* 0.7

# enemy vehicle
car2 = pygame.image.load('otherCar.png')
car_loc2 = car.get_rect()
car_loc2.center = left_lane, height* 0.2


while running:
    # Animate enemy car
    car_loc2[1] += speed
    if car_loc2[1] > height:
        # randomly select lane
        if random.randint(0,1) == 0:
            car_loc2.center = right_lane, -200
        else:
            car_loc2.center = left_lane, -200


    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move(int(road_w/2), 0)
        # TODO: add restriction to car movements

    pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2-road_w/2, 0, road_w, height)
    )

    # center yellow line
    pygame.draw.rect(
        screen,
        (255, 240, 60),
        (width/2 - roadmark_w/2, 0, roadmark_w, height)
    )

    # left white line
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 - road_w/2 + roadmark_w * 2, 0, roadmark_w, height)
    )

    #right white line
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (width/2 + road_w/2 - roadmark_w * 3, 0, roadmark_w, height)
    )

    screen.blit(car, car_loc)
    screen.blit(car2, car_loc2)
    pygame.display.update()

pygame.quit()
