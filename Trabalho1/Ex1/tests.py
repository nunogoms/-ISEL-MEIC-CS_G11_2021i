import unittest

from spartan_scytale import spartan_scytale_cipher


class TestCases(unittest.TestCase):
    def test_exercise1a(self):
        entry = "abatalhacomospersasteralugarnodesfiladeirodastermopilas"
        n = 4
        result = "AENDBROAASDSTAETASSELTFRHEIMARLOCAAPOLDIMUELOGIASARSPRO"
        self.assertEqual(result, spartan_scytale_cipher(entry, n))

    def test_ppt_example(self):
        entry = "acitalaeumsistemadecifrausadonaantigagrecia"
        n = 5
        result = "AMEDACSCOGIIINRTSFAEATRACLEANIAMUTAEASIUDAG"
        self.assertEqual(result, spartan_scytale_cipher(entry, n), result)
