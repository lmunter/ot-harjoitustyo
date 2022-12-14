import random
import pygame

class Platform(pygame.sprite.Sprite):
    """Class for managing the platforms on which the player travels.

    Attributes:
        width: the x-dimension of the platform
        surf: pygame surface-object of the platform
        rect: contains dimensions and positional coordinates
    """
    def __init__(self):
        super().__init__()
        self.width = random.randint(1300, 1700)
        self.surf = pygame.Surface((self.width, 50))
        self.surf.fill((10, 10, 10))
        self.rect = self.surf.get_rect()
        self.rect.x = 0
        self.rect.y = 930
