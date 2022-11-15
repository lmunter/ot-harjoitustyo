import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        kortti = Maksukortti(1000)
	
    def test_konstruktori_asettaa_saldon_oikein(self):
	self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")
	
    def test_syo_edullisesti_vahentaa_saldoa_oikein(self):
	kortti.syo_edullisesti()
	self.assertEqual(str(kortti), "Kortilla on rahaa 7.50 euroa")

    def test_syo_maukkaasti_vahentaa_saldoa_oikein(self):
    	kortti.syo_maukkaasti()
    	self.assertEqual(str(kortti), "Kortilla on rahaa 6.00 euroa")

    def test_syo_edullisesti_ei_vie_saldoa_negatiiviseksi(self):
    	kortti = Maksukortti(200)
    	kortti.syo_edullisesti()
    	self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_kortille_voi_ladata_rahaa(self):
    	self.kortti.lataa_rahaa(2500)
    	self.assertEqual(str(self.kortti), "Kortilla on rahaa 35.00 euroa")

    def test_kortin_saldo_ei_ylita_maksimiarvoa(self):
    	self.kortti.lataa_rahaa(20000)
    	self.assertEqual(str(self.kortti), "Kortilla on rahaa 150.00 euroa")

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
	kortti = Maksukortti(200)
	kortti = syo_maukkaasti()
	self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def	test_ei_voi_ladata_negatiivista_saldoa(self):
	self.kortti.lataa_rahaa(-1000)
	self.assertEqual(str(kortti), "Kortilla on rahaa 10.00 euroa")
