import unittest
from remove_vowels import remove_vowels  

class TestRemoveVowels(unittest.TestCase):

    def test_no_vowels(self):
        self.assertEqual(remove_vowels("Hello, World!"), "Hll, Wrld!")

    def test_all_vowels(self):
        self.assertEqual(remove_vowels("AEIOU"), "")

    def test_no_vowels_in_string(self):
        self.assertEqual(remove_vowels("bcd"), "bcd")

    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_mixed_case(self):
        self.assertEqual(remove_vowels("HeLLo"), "HLL")

    def test_spaces_and_punctuation(self):
        self.assertEqual(remove_vowels("Hello, how are you?"), "Hll, hw r y?")

if __name__ == "__main__":
    unittest.main()
