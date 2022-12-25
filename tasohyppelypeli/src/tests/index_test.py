import unittest
import pygame
from index import Game
from my_platform import Platform
from player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(testing = True)
        self.platform1 = Platform()
        self.platform2 = Platform()
        self.player = Player()
    
    def test_gravity_not_pulling_when_player_is_on_platform(self):
        for i in range(1, 3):
            self.game.gravity(self.player, self.platform1, self.platform2)
        self.assertEqual(self.game.can_jump, True)
    
    def test_platforms_are_recycled(self):
        self.game.platform1.rect.x = -self.game.platform1.width
        self.game.recycle_platforms()
        self.assertEqual(self.game.platform1.rect.x, self.game.platform2.width+200)

    def test_new_high_scores_are_recorded(self):
        test = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_t, unicode="t")
        pygame.event.post(test)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN))
        self.game.check_user_input(testing = True)
        self.assertEqual(len(self.game.high_scores), 1)
    
    def test_high_scores_are_rendered_correctly(self):
        self.game.high_scores.append(("test", 100))
        test = self.game.render_high_scores(100, 100)
        print(test)
        self.assertEqual((test.x, test.y), (110, 110))