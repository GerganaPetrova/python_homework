import unittest

import solution


class TestFiveFunctions(unittest.TestCase):

    def test_sort_by(self):
        words = ['hey', 'hi', 'hello', 'buy', 'io', 'a']
        self.assertEqual(
            ['a', 'hi', 'io', 'hey', 'buy', 'hello'],
            solution.sort_by(lambda x, y: len(x) - len(y), words))

        self.assertEqual(
            [3, 3, 5, 10, 15, 30, 100],
            solution.sort_by(lambda x, y: x - y,
                             [15, 3, 10, 100, 5, 3, 30]))

        self.assertEqual(
            [1, 2, 7, 9, 15, 32, 33],
            solution.sort_by(lambda x, y: x - y,
                             [7, 2, 9, 1, 15, 33, 32]))

        self.assertEqual(
            [0, 4, 4, 5, 11, 12, 16],
            solution.sort_by(lambda x, y: x - y,
                             [12, 5, 4, 16, 0, 4, 11]))

    def test_group_by_type(self):
        self.assertEqual(
            {str: {'val': 5, 'var': 7}, int: {1: 2},
                   tuple: {(3, 4): 'c'}},
            solution.group_by_type({'val': 5, 'var': 7, 1: 2,
                                   (3, 4): 'c'}))

        self.assertEqual(
            {str: {'c': 15}, int: {1: 'b', 12: 202},
             tuple: {(1, 2): 12, ('a', 1): 1, (3, 4, 5, 6): 7}},
            solution.group_by_type({(1, 2): 12, ('a', 1): 1, 1: 'b',
                                    (3, 4, 5, 6): 7, 'c': 15, 12: 202}))

    def test_anagrams(self):
        words = ['woman hitler', 'the eyes', 'dormitory', 'mother-in-law',
                 'dirty room', 'they see']
        anagrams = [['woman hitler', 'mother-in-law'],
                    ['the eyes', 'they see'],
                    ['dormitory', 'dirty room']]

        self.assertEqual(
            set(map(frozenset, anagrams)),
            set(map(frozenset, solution.anagrams(words))))


if __name__ == '__main__':
    unittest.main()
