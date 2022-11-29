import unittest
import os
from index import Pelaaja

class TestPelaaja(unittest.TestCase):
    def setUp(self):
        self.pelaaja = Pelaaja()
    
    def test_pelaajalla_on_oikea_sprite(self):
        dirname = os.path.dirname(__file__)
        polku = os.path.split(dirname)
        odotettu_tulos = os.path.join(polku[0], "assets", "pelaaja.jpg")
        self.assertEqual(self.pelaaja.image, odotettu_tulos)