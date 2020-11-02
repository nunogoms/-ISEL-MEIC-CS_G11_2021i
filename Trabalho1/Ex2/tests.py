import unittest

from cipher import belaso_vigenere


class MyTestCase(unittest.TestCase):

    def test_first_user_case(self):
        result = belaso_vigenere("primeiracifrapolialfabeticacomtrocadechave", "ZAR")
        expected = ["O", "R", "Z", "L", "E", "Z", "Q", "A", "T", "H", "F", "I", "Z", "P", "F", "K", "I", "R", "K", "F",
                    "R", "A", "E", "K", "H", "C", "R", "B", "O", "D", "S", "R", "F", "B", "A", "U", "D", "C", "Y", "Z",
                    "V", "V"]

        self.assertEqual(expected, result)

    def test_second_user_case(self):
        result = belaso_vigenere("acifradebelaso", "BELASOBELASOBE")
        expected = ["B", "G", "T", "F", "J", "O", "E", "I", "M", "E", "D", "O", "T", "S"]
        self.assertEqual(expected, result)

    def test_third_user_case(self):
        result = belaso_vigenere("attackatdawn", "LEMONLEMONLE")
        expected = ["L", "X", "F", "O", "P", "V", "E", "F", "R", "N", "H", "R"]
        self.assertEqual(expected, result)

    def test_fourth_user_case(self):
        result = belaso_vigenere("defendtheeastwallofthecastle", "FORTIFICATIONFORTIFICATIONFO")
        expected = ["I", "S", "W", "X", "V", "I", "B", "J", "E", "X", "I", "G", "G", "B", "O", "C", "E", "W", "K", "B",
                    "J", "E", "V", "I", "G", "G", "Q", "S"]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
