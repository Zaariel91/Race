import pygame
import time
import random
from pygame.colordict import THECOLORS
from barrier import Barrier, Haystack
 
pygame.init()

time_step = 4000
pygame.time.set_timer(pygame.USEREVENT, time_step)
 
W = 900
H = 780
 
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("События от клавиатуры")
# pygame.display.set_icon(pygame.image.load("app.bmp"))


FPS = 60
clock = pygame.time.Clock()
 
x = W // 2
y = H // 2
speed = 5
car_speed = 5
score = 0

field_stage1 = pygame.image.load('images/field.bmp')
field_stage2 = pygame.image.load('images/field_stage2.jpg')
road = pygame.image.load('images/road.jpg')
road_rect = road.get_rect(center = (x, y))

car = pygame.image.load('images/car.png').convert()
car.set_colorkey(THECOLORS['white'])
car_rect = car.get_rect(center = (x, y + 320))

line_1 = pygame.draw.line(road, THECOLORS['white'], (10, 0), (10, 800), 5)
line_2 = pygame.draw.line(road, THECOLORS['white'], (160, 0), (160, 800), 5)
line_3 = pygame.draw.line(road, THECOLORS['white'], (308, 0), (308, 800), 5)
line_4 = pygame.draw.line(road, THECOLORS['white'], (460, 0), (460, 800), 5)
line_down = pygame.draw.line(road, THECOLORS['white'], (0, 800), (900, 800), 5)


balls = pygame.sprite.Group()

def createBall(group):
    global score
    x = random.choice([W // 2 - 150, W // 2, W // 2 + 150])
    speed = 3
        
    return Barrier(x, speed, score, group)

def createHaystack(group):
    global score
    x = random.choice([W // 2 - 150, W // 2, W // 2 + 150])
    speed = 3
        
    return Haystack(x, speed, score, group)


def collideBalls():
    global score
    for ball in balls:
        if line_down.collidepoint(ball.rect.center):
            score += 5
            ball.kill()

paused = False
createBall(balls)
createBall(balls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            if score <= 20:
                createBall(balls)
                createBall(balls)
            elif score <= 250:
                createHaystack(balls)
                createHaystack(balls)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
    if paused == True:
        continue        
    mv = pygame.key.get_pressed()

    if mv[pygame.K_LEFT]:
        car_rect.x -= car_speed
    if car_rect.x < 230:
        car_rect.x = 230
    elif mv[pygame.K_RIGHT]:
        car_rect.x += car_speed
        if car_rect.x > 600:
            car_rect.x = 600
    elif mv[pygame.K_UP]:
        car_rect.y -= car_speed
        if car_rect.y < 0:
            car_rect.y = 0
    elif mv[pygame.K_DOWN]:
        car_rect.y += car_speed
        if car_rect.y > 650:
            car_rect.y = 650


    collideBalls()

    if score <= 20:
        sc.blit(field_stage2, (0 ,0))
    elif score <= 250:
        sc.blit(field_stage1, (0 ,0))

    sc.blit(road, road_rect)
    balls.draw(sc)
    sc.blit(car, car_rect)
    pygame.display.update()
    balls.update(H)
    
    clock.tick(FPS)