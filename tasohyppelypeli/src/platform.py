import pygame
import random

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super(Platform, self).__init__()
        self.width = random.randint(1300, 1700)
        self.surf = pygame.Surface((self.width, 50))
        self.surf.fill((10, 10, 10))
        self.rect = self.surf.get_rect()
        self.rect.x = 0
        self.rect.y = 1030
