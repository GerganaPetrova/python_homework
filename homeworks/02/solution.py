import string
from collections import defaultdict
from functools import cmp_to_key

ALPHABET = set('абвгдежзийклмнопрстуфхцчшщъьюя')


def is_cyrillic_letter(x):
    return x in ALPHABET


def is_pangram(sentence):
    return set(filter(is_cyrillic_letter, sentence.lower())) == ALPHABET


def char_histogram(text):
    return {char: text.count(char) for char in text}


def sort_by(func, arguments):
    return sorted(arguments, key=cmp_to_key(func))


def group_by_type(dictionary):
    result = defaultdict(dict)
    for key, value in dictionary.items():
        result[type(key)].update({key: value})
    return result


def is_letter(x):
    return x not in (string.punctuation + string.whitespace)


def is_anagram(word1, word2):
    word1 = sorted(filter(is_letter, word1.lower()))
    word2 = sorted(filter(is_letter, word2.lower()))
    return word1 == word2


def word_anagrams(word, words):
    return list(filter(lambda x: is_anagram(x, word), words))


def anagrams(words):
    return list(map(lambda x: word_anagrams(x, words), words))
