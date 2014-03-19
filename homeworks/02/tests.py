import unittest
import solution
from solution import is_pangram, char_histogram, sort_by, group_by_type

class TestFiveFunctions(unittest.TestCase):
    # sample tests
    def test_is_pangram(self):
        self.assertFalse(
            is_pangram('Малката пухкава панда яде бамбук.'))

        self.assertTrue(
            is_pangram(
                'Ах, чудна българска земьо, полюшвай цъфтящи жита!'))
    def test_is_pangram_uppercase_1(self):
        self.assertTrue(
            is_pangram('АБВ ГДЕЖЗ ЯЮъьЩшчц ийКлМН опрстуфьдх'))

    def test_is_pangram_uppercase_2(self):
        self.assertTrue(
            is_pangram(
                'Ах, чудна българска земьо, полюшвай цъфтящи жита!'.upper()))

    def  test_is_pangram_english_letters(self):
        self.assertFalse(
            is_pangram('Ах, чудна българска зеmьо, полюшвай цъфтящи жита!')
        )

    def test_char_histogram(self):
        self.assertEqual(
            {' ': 3, 'i': 2, 'a': 2, 'e': 2, 's': 2, 'h': 1, 'l': 1, 'm': 1,
             'n': 1, 'x': 1, '!': 1, 'p': 1, 'T': 1},
            char_histogram('This is an example!'))

    def test_char_histogram(self):
        self.assertEqual(char_histogram(
            'Ах, чудна българска зеmьо, полюшвай цъфтящи жита!'),
                         {'m': 1, ',': 2, '!': 1, ' ': 6, 'л': 2, 'к': 1, 'й': 1, 'и': 2, 'п': 1, 'о': 2, 'н': 1, 'г': 1,
                          'в': 1, 'б': 1, 'а': 5, 'з': 1, 'ж': 1, 'е': 1, 'д': 1, 'ъ': 2, 'щ': 1, 'ш': 1, 'я': 1, 'ю': 1,
                          'ь': 1, 'у': 1, 'т': 2, 'с': 1, 'р': 1, 'ч': 1, 'ц': 1, 'х': 1, 'ф': 1, 'А': 1})

    def test_char_histogram_10a_3b(self):
        self.assertEqual(char_histogram('aaaabbaaaabaa'), {'a': 10, 'b': 3})


    def test_sort_by(self):
        self.assertEqual(
            ['a', 'ab', 'abc'], sort_by(lambda x, y: len(x) - len(y), ['abc', 'a', 'ab']))

    def test_sort_by_2(self):
        self.assertEqual(sort_by(lambda x, y: len(y) - len(x), ['abc', 'a', 'ab', 'Pesho', [1, 2, 3, 4]]), ['Pesho', [1, 2, 3, 4], 'abc', 'ab', 'a'])

    def test_group_by_type(self):
        self.assertEqual(
            {str: {'b': 1, 'a': 12}, int: {1: 'foo'}},
            group_by_type({'a': 12, 'b': 1, 1: 'foo'}))

        self.assertEqual(
            {str: {'c': 15}, int: {1: 'b'},
             tuple: {(1, 2): 12, ('a', 1): 1}},
            group_by_type({(1, 2): 12, ('a', 1): 1, 1: 'b', 'c': 15}))


    def test_group_by_type_2(self):
        self.assertEqual(group_by_type({int: 2, str: 'a', (1,): [1, 2], 'a': (1, 'v')}),
        {type: {str: 'a', int: 2}, tuple: {(1,): [1, 2]}, str: {'a': (1, 'v')}})

    def test_anagrams(self):
        words = ['army', 'mary', 'ramy', 'astronomer', 'moonstarer',
                 'debit card', 'bad credit', 'bau']
        anagrams = [['army', 'mary', 'ramy'],
                    ['bad credit', 'debit card'],
                    ['astronomer', 'moonstarer'], ['bau']]
        self.assertEqual(
            set(map(frozenset, anagrams)),
            set(map(frozenset, solution.anagrams(words))))

    def test_anagrams_2(self):
        words = ['listen', 'are', 'pets', 'inlets', 'ear', 'enlist',
                 'step', 'pest', 'silent', 'tinsel', 'era']
        anagrams = [['listen', 'inlets', 'enlist', 'silent', 'tinsel'],
                    ['are', 'ear', 'era'],
                    ['pets', 'step', 'pest']]
        self.assertEqual(
            set(map(frozenset, anagrams)),
            set(map(frozenset, solution.anagrams(words))))

if __name__ == '__main__':
    unittest.main()
