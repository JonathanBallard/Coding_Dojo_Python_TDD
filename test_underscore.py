import unittest
from underscore import Underscore
class UnderscoreTest(unittest.TestCase):
    def setUp(self):
        # create an instance of the Underscore module we created
        self._ = Underscore()
        # initialize a list to run our tests on
        self.test_list = [1,2,3,4,5]
    def testMap(self):
        return self.assertEqual([1,4,9,16,25], self._.map(self.test_list, lambda x : x ** 2))
    def testReduce(self):
        return self.assertEqual(15, self._.reduce(self.test_list, lambda x,y : x + y, 0))
    def testFind(self):
        if self.assertEqual(True, self._.find(self.test_list, lambda x : 5)):
            return self.assertEqual(True, self._.find(self.test_list, lambda x : 5))
        elif self.assertEqual(True, self._.find(self.test_list, lambda x : 4)):
            return self.assertEqual(True, self._.find(self.test_list, lambda x : 4))
        elif self.assertEqual(True, self._.find(self.test_list, lambda x : 3)):
            return self.assertEqual(True, self._.find(self.test_list, lambda x : 3))
        elif self.assertEqual(True, self._.find(self.test_list, lambda x : 2)):
            return self.assertEqual(True, self._.find(self.test_list, lambda x : 2))
        elif self.assertEqual(True, self._.find(self.test_list, lambda x : 1)):
            return self.assertEqual(True, self._.find(self.test_list, lambda x : 1))
        else:
            return self.assertEqual(True, self._.find(self.test_list, lambda x : 5 or 1 or 2 or 3 or 4))
    def testFilter(self):
        return self.assertEqual([1,2], self._.filter(self.test_list, lambda x : x <= 2))
    def testReject(self):
        return self.assertEqual([1,2], self._.reject(self.test_list, lambda x : x > 2))


if __name__ == "__main__":
    unittest.main()
