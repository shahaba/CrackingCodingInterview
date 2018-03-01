import unittest
from LongestPalindrome import longestPalindrome


class TestPalindrome(unittest.TestCase):


    def testEmpty(self):
        self.assertEqual(longestPalindrome(''), '')


    def testOneLetter(self):
        self.assertEqual(longestPalindrome('a'), 'a')


    def testTwoLetters(self):
        self.assertEqual(longestPalindrome('aa'), 'aa')


    def testEvenLetterTrue(self):
        self.assertEqual(longestPalindrome('aabbccddaa'), 'aacbddbcaa')


    def testOddLetterTrue(self):
        self.assertEqual(longestPalindrome('aba'), 'aba')



if __name__ == '__main__':
    unittest.main()