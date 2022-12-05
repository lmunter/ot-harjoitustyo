import pygame
import os

dirname = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = os.path.join(dirname, "assets", "pelaaja.jpg")
        self.surf = pygame.image.load(self.image)
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 50
        self.rect.y = 980
    
    def jump(self):
        jump = True
        while jump:
            while self.rect.y > 780:
                self.rect.y -= 1
            jump = False