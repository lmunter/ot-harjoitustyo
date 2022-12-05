import unittest
from my_platform import Platform

class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = Platform()
    
    def test_two_platforms_do_not_have_same_width(self):
        self.platform2 = Platform()
        self.assertNotEqual(self.platform.width, self.platform2.width)