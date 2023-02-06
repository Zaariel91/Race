import pygame
from pygame.colordict import THECOLORS


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, speed, filename) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image.set_colorkey(THECOLORS['white'])
        self.rect = self.image.get_rect(center = (x, 0))
        self.speed = speed

    def update(self, *args) -> None:
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.rect.y = 0