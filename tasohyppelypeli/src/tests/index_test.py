import unittest
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