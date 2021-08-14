import unittest
from src import function


class PalindromeOptimized(unittest.TestCase):
    PALINDROME = "abba"
    NOT_PALINDROME = "abba3"

    def test_whenPalindromePass_returnTrue(self):
        self.assertTrue(function.is_palindrome_optimized(self.PALINDROME))

    def test_whenPalindromeNotPass_returnFalse(self):
        self.assertFalse(function.is_palindrome_optimized(self.NOT_PALINDROME))


class PalindromeQueue(unittest.TestCase):
    PALINDROME = "abba"
    NOT_PALINDROME = "abba3"

    def test_whenPalindromePass_returnTrue(self):
        self.assertTrue(function.is_palindrome_queue(self.PALINDROME))

    def test_whenPalindromeNotPass_returnFalse(self):
        self.assertFalse(function.is_palindrome_queue(self.NOT_PALINDROME))


class PalindromeReverse(unittest.TestCase):
    PALINDROME = "abba"
    NOT_PALINDROME = "abba3"

    def test_whenPalindromePass_returnTrue(self):
        self.assertTrue(function.is_palindrome_reverse(self.PALINDROME))

    def test_whenPalindromeNotPass_returnFalse(self):
        self.assertFalse(function.is_palindrome_reverse(self.NOT_PALINDROME))


if __name__ == '__main__':
    unittest.main()
