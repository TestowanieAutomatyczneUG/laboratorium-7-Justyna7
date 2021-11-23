import unittest
import sys
sys.path.insert(1, '..')
from main import *


class PasswordTest(unittest.TestCase):

    def setUp(self):
        self.temp = Password()

    def test_Pass_too_short(self):
        self.assertEqual(False, self.temp.ValidPassword("Merkury"))

    def test_Pass_Teeeeeeest3(self):
        self.assertEqual(False, self.temp.ValidPassword("Teeeeeeest3"))

    def test_Pass_Teeeeeeest3plus(self):
        self.assertEqual(True, self.temp.ValidPassword("Teeeeeeest3+"))

    def test_Pass_Teeeeeeest(self):
        self.assertEqual(False, self.temp.ValidPassword("Teeeeeeest"))

    def test_Pass_Teeeeeeest2345_(self):
        self.assertEqual(True, self.temp.ValidPassword("Teeeeeeest2345_"))

    def test_Pass_onluNum(self):
        self.assertEqual(False, self.temp.ValidPassword("333425364787564"))

    def test_Pass_1TeUeee34ee_esGHt25(self):
        self.assertEqual(True, self.temp.ValidPassword("1Te&Uee+e34ee_esG*Ht25"))

    def test_Pass_obj(self):
        self.assertEqual(False, self.temp.ValidPassword({}))

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()
