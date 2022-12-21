import os
import pygame

dirname = os.path.dirname(__file__)

class Player(pygame.sprite.Sprite):
    """Class for managing the player character.

    Attributes:
        image: picture of the player character to display on screen
        surf: pygame surface-object of the player
        rect: contains dimensions and positional coordinates
    """
    def __init__(self):
        super().__init__()
        self.image = os.path.join(dirname, "assets", "pelaaja.jpg")
        self.surf = pygame.image.load(self.image)
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.x = 50
        self.rect.y = 880

    def jump(self):
        """Lifts the player to a specific height.

        """
        jump = True
        while jump:
            while self.rect.y > 680:
                self.rect.y -= 1
            jump = False
