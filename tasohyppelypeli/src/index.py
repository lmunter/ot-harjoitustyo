import sys
import pygame
from my_platform import Platform
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.player = Player()
        self.platform = Platform()
        self.platform2 = Platform()
        self.platform2.rect.x = self.platform.width + 100
        self.can_jump = True
        self.points = 0
        self.high_scores = []

        self.screen = pygame.display.set_mode([1920, 1080])
        pygame.display.set_caption("Skeittaaja rotkoon")
        self.main_menu()

    def main_menu(self):
        main_menu_text = self.font.render("Skeittaaja rotkoon", True, (0, 0, 0))
        main_menu_instructions = self.font.render(
            "F2 - Uusi peli    ESC - Sulje peli", True, (0, 0, 0)
            )
        self.screen.fill((235, 235, 235))
        self.screen.blit(main_menu_text, (660, 340))
        self.screen.blit(main_menu_instructions, (660, 440))
        pygame.display.flip()
        while True:
            self.check_events()

    def new_game(self):
        self.points = 0
        self.player.rect.y = 880
        self.platform.rect.x = 0
        self.platform2.rect.x = self.platform.width + 100
        while True:
            self.check_events()

            self.gravity(self.player, self.platform, self.platform2)

            self.platform.rect.x -= 3
            self.platform2.rect.x -= 3
            self.recycle_platforms()

            self.screen.fill((235, 235, 235))
            points_text = self.font.render(f"Score: {self.points}", True, (0, 0, 0))
            self.screen.blit(self.player.surf, self.player.rect)
            self.screen.blit(self.platform.surf, self.platform.rect)
            self.screen.blit(self.platform2.surf, self.platform2.rect)
            self.screen.blit(points_text, (1800, 0))
            pygame.display.flip()
            self.points += 1

            self.clock.tick(60)

            if self.player.rect.y >= 980:
                self.game_over()

    def game_over(self):
#        for high_score in self.high_scores:
#            if self.points > high_score[1]:
        self.screen.fill((235, 235, 235))
        game_over_text = self.font.render("Game Over", True, (0, 0, 0))
        game_over_instructions = self.font.render(
            "F2 - Uusi peli    ESCAPE - Sulje peli", True, (0, 0, 0)
            )
        self.screen.blit(game_over_text, (660, 440))
        self.screen.blit(game_over_instructions, (660, 540))
        pygame.display.flip()
        while True:
            self.check_events()

    def recycle_platforms(self):
        if self.platform.rect.x <= -(self.platform.width):
            self.platform = Platform()
            self.platform.rect.x = self.platform2.width + 200
        if self.platform2.rect.x <= -(self.platform2.width):
            self.platform2 = Platform()
            self.platform2.rect.x = self.platform.width + 200

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_pressed_keys(event)

    def check_pressed_keys(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            if self.can_jump:
                self.player.jump()
        elif event.key == pygame.K_F2:
            self.new_game()

    def gravity(self, player, platform1, platform2):
        sprite_list = [player]
        if player not in pygame.sprite.spritecollide(platform1, sprite_list, False) \
        and player not in pygame.sprite.spritecollide(platform2, sprite_list, False):
            self.can_jump = False
            self.player.rect.y += 4
        else:
            self.can_jump = True

if __name__ == "__main__":
    Game()
