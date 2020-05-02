

import unittest
# https://docs.python.org/2/library/unittest.html#unittest.TestCase

def isEven(n):
    return n % 2 == 0




class isEvenTests(unittest.TestCase):
    def testTwo(self):
        self.failUnless(isEven(2))
    def testThree(self):
        self.failIf(isEven(3))


if __name__ == '__main__':
    unittest.main()




