import pygame
from pygame.colordict import THECOLORS


class Barrier(pygame.sprite.Sprite):
    def __init__(self, x, speed, surf, group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image.set_colorkey(THECOLORS['white'])
        self.rect = self.image.get_rect(center = (x, 0))
        self.speed = speed
        self.add(group)

    def update(self, *args) -> None:
        if self.rect.y < args[0] - 20:
            self.rect.y += self.speed
        else:
            self.kill()