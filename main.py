import pygame
import time
import random
from pygame.colordict import THECOLORS
from barrier import Barrier
 
pygame.init()
 
W = 900
H = 780
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от клавиатуры")
# pygame.display.set_icon(pygame.image.load("app.bmp"))
 

FPS = 60        # число кадров в секунду
clock = pygame.time.Clock()
 
x = W // 2
y = H // 2
speed = 5
car_speed = 15

field = pygame.image.load('images/field.bmp')

road = pygame.image.load('images/road.jpg')
road_rect = road.get_rect(center = (x, y))

car = pygame.image.load('images/car.png'   ).convert()
car.set_colorkey(THECOLORS['white'])
car_rect = car.get_rect(center = (x, y + 320))

line_1 = pygame.draw.line(road, THECOLORS['white'], (10, 0), (10, 800), 5)
line_2 = pygame.draw.line(road, THECOLORS['white'], (160, 0), (160, 800), 5)
line_3 = pygame.draw.line(road, THECOLORS['white'], (308, 0), (308, 800), 5)
line_4 = pygame.draw.line(road, THECOLORS['white'], (460, 0), (460, 800), 5)

barrier_1 = Barrier(x - 150, speed, 'images/barrier_150.png')
barrier_2 = Barrier(x, speed, 'images/barrier_150.png')
barrier_3 = Barrier(x + 150, speed, 'images/barrier_150.png')



while True:
    line_1 = pygame.draw.line(road, THECOLORS['white'], (10, 0), (10, 800), 5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    mv = pygame.key.get_pressed()
    if mv[pygame.K_LEFT]:
        car_rect.x -= speed
        if car_rect.x < 230:
            car_rect.x = 230
    elif mv[pygame.K_RIGHT]:
        car_rect.x += speed
        if car_rect.x > 600:
            car_rect.x = 600
    elif mv[pygame.K_UP]:
        car_rect.y -= speed
        if car_rect.y < 0:
            car_rect.y = 0
    elif mv[pygame.K_DOWN]:
        car_rect.y += speed
        if car_rect.y > 650:
            car_rect.y = 650

    sc.blit(field, (0 ,0))
    sc.blit(road, road_rect)
    sc.blit(car, car_rect)
    sc.blit(barrier_1.image, barrier_1.rect)
    sc.blit(barrier_2.image, barrier_2.rect)
    sc.blit(barrier_3.image, barrier_3.rect)

    pygame.display.update()

    barrier_1.update(H)
    barrier_2.update(H)
    barrier_3.update(H)
    # sc.fill(THECOLORS['white'])
    # # pygame.draw.rect(sc, THECOLORS['white'], (x, y, 10, 20))
    # rect = pygame.Rect(0, 0, 250, 250)
    # rect.center = (x, y)
    # pygame.draw.rect(sc, THECOLORS['black'], rect, 5)
    # pygame.draw.aaline(sc, THECOLORS['black'], (x, y - 350), (x -50, y + 50))
    # pygame.draw.aaline(sc, THECOLORS['black'], (x, 800), (x, 0))

    # pygame.display.update()
 
    clock.tick(FPS)