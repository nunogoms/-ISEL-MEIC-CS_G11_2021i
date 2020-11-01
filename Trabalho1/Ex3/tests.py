import unittest

from lfsr import generate_keystream


class MyTestCase(unittest.TestCase):

    def test_first_relation_with_6_elements(self):
        relation = [1, 1]
        initial_sequence = [1, 0]

        expected = [1, 0, 1, 1, 0, 1]
        current = generate_keystream(relation, initial_sequence, 6)

        self.assertEqual(expected, current)

    def test_first_relation_with_9_elements(self):
        relation = [1, 1]
        initial_sequence = [0, 1]

        expected = [0, 1, 1, 0, 1, 1, 0, 1, 1]
        current = generate_keystream(relation, initial_sequence, 9)

        self.assertEqual(expected, current)

    def test_first_relation_with_16_elements(self):
        relation = [1, 1]
        initial_sequence = [1, 0]

        expected = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
        current = generate_keystream(relation, initial_sequence, 16)

        self.assertEqual(expected, current)

    def test_second_relation_with_6_elements(self):
        relation = [0, 1, 1]
        initial_sequence = [0, 1, 0]

        expected = [0, 1, 0, 1, 1, 1]
        current = generate_keystream(relation, initial_sequence, 6)

        self.assertEqual(expected, current)

    def test_second_relation_with_9_elements(self):
        relation = [0, 1, 1]
        initial_sequence = [0, 1, 1]

        expected = [0, 1, 1, 1, 0, 0, 1, 0, 1]
        current = generate_keystream(relation, initial_sequence, 9)

        self.assertEqual(expected, current)

    def test_second_relation_with_16_elements(self):
        relation = [0, 1, 1]
        initial_sequence = [1, 0, 0]

        expected = [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0]
        current = generate_keystream(relation, initial_sequence, 16)

        self.assertEqual(expected, current)

    def test_third_relation_with_6_elements(self):
        relation = [0, 1, 0, 1, 1]
        initial_sequence = [0, 0, 1, 0, 0]

        expected = [0, 0, 1, 0, 0, 0]
        current = generate_keystream(relation, initial_sequence, 6)

        self.assertEqual(expected, current)

    def test_third_relation_with_9_elements(self):
        relation = [0, 1, 0, 1, 1]
        initial_sequence = [0, 1, 1, 0, 1]

        expected = [0, 1, 1, 0, 1, 1, 1, 0, 0]
        current = generate_keystream(relation, initial_sequence, 9)

        self.assertEqual(expected, current)

    def test_third_relation_with_16_elements(self):
        relation = [0, 1, 0, 1, 1]
        initial_sequence = [1, 1, 0, 0, 1]

        expected = [1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1]
        current = generate_keystream(relation, initial_sequence, 16)

        self.assertEqual(expected, current)


if __name__ == '__main__':
    unittest.main()
