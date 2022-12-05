import unittest
import os
from index import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
    
    def test_player_has_correct_sprite(self):
        dirname = os.path.dirname(__file__)
        path = os.path.split(dirname)
        expected = os.path.join(path[0], "assets", "pelaaja.jpg")
        self.assertEqual(self.player.image, expected)