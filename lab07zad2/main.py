# import unittest
import re


class Password:
    def ValidPassword(self, p):
        if type(p) == str:
            if len(p) >= 8:
                return bool(re.search(r"[a-z]+", p)) and bool(re.search(r"[A-Z]+", p)) \
                    and bool(re.search(r"[0-9]+", p)) and bool(re.search(r"[\W_]+", p))
            else:
                return False
        else:
            return False


# class PasswordTest(unittest.TestCase):
#
#     def setUp(self):
#         self.temp = Password()
#
#     def test_Pass_too_short(self):
#         self.assertEqual(False, self.temp.ValidPassword("Merkury"))
#
#     def test_Pass_Teeeeeeest3(self):
#         self.assertEqual(False, self.temp.ValidPassword("Teeeeeeest3"))
#
#     def test_Pass_Teeeeeeest3plus(self):
#         self.assertEqual(True, self.temp.ValidPassword("Teeeeeeest3+"))
#
#     def test_Pass_Teeeeeeest(self):
#         self.assertEqual(False, self.temp.ValidPassword("Teeeeeeest"))
#
#     def test_Pass_Teeeeeeest2345_(self):
#         self.assertEqual(True, self.temp.ValidPassword("Teeeeeeest2345_"))
#
#     def test_Pass_onluNum(self):
#         self.assertEqual(False, self.temp.ValidPassword("333425364787564"))
#
#     def test_Pass_1TeUeee34ee_esGHt25(self):
#         self.assertEqual(True, self.temp.ValidPassword("1Te&Uee+e34ee_esG*Ht25"))
#
#     def test_Pass_obj(self):
#         self.assertEqual(False, self.temp.ValidPassword({}))
#
#     def tearDown(self):
#         self.temp = None
#
#
# if __name__ == '__main__':
#     unittest.main()
