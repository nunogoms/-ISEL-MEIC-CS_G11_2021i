import unittest

from one_and_zeroes import padd_oneandzeroes, unpadd_oneandzeroes
from trailing_bit_complement import padd_trailingbitcom, unpadd_trailingbitcom


def intlist_tostring(array: list[int]):
    result_str = "["
    for i in range(0, len(array) - 1):
        result_str += array[i].__str__() + ","

    result_str += array[len(array) - 1].__str__() + "]"

    return result_str


class OneAndZeroesTestCases(unittest.TestCase):
    def test_padding_4bits(self):
        entry = [1, 0, 0, 0]
        n = 4
        result = [1, 0, 0, 0, 1, 0, 0, 0]
        self.assertEqual(result, padd_oneandzeroes(entry, n))

    def test_padding_6ai1(self):
        entry = [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
        n = 8
        result = [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0]
        self.assertEqual(result, padd_oneandzeroes(entry, n))

    def test_padding_6ai2(self):
        entry = [0, 0, 1, 0, 1, 1, 1, 1]
        n = 8
        result = [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result, padd_oneandzeroes(entry, n))

    def test_unpadding_6aiii(self):
        entry = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
        n = 4
        result = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
        self.assertEqual(result, unpadd_oneandzeroes(entry, n))

    def test_unpadding_8bits(self):
        entry = [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        n = 8
        result = [0, 0, 1, 0, 0, 1, 1, 1]
        self.assertEqual(result, unpadd_oneandzeroes(entry, n))


class TrailingBitComplementTestCases(unittest.TestCase):
    def test_padding_4bits(self):
        entry = [1, 0, 0, 0]
        n = 4
        result = [1, 0, 0, 0, 1, 1, 1, 1]
        self.assertEqual(result, padd_trailingbitcom(entry, n))

    def test_padding_6aii1(self):
        entry = [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1]
        n = 8
        result = [0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
        self.assertEqual(result, padd_trailingbitcom(entry, n))

    def test_padding_6aii2(self):
        entry = [0, 0, 1, 0, 1, 1, 1, 1]
        n = 8
        result = [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result, padd_trailingbitcom(entry, n))

    def test_unpadding_6aiii(self):
        entry = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
        n = 4
        result = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]
        self.assertEqual(result, unpadd_trailingbitcom(entry, n))

    def test_unpadding_8bits(self):
        entry = [0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
        n = 8
        result = [0, 0, 1, 0, 0, 1, 1, 1]
        self.assertEqual(result, unpadd_trailingbitcom(entry, n))


def main():
    OneAndZeroesTestCases()
    TrailingBitComplementTestCases()


if __name__ == '__main__':
    main()
