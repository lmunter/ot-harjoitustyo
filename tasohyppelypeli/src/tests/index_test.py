import unittest
from index import Game
from my_platform import Platform
from player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.platform1 = Platform()
        self.platform2 = Platform()
        self.player = Player()
    
    def test_gravity_not_pulling_when_player_is_on_platform(self):
        self.game.gravity(self.player, self.platform1, self.platform2)
        self.assertEqual(self.player.can_jump, True)