import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        # These are the test cases for max_list
        tlist = None
        with self.assertRaises(ValueError):                                         # used to check for exception, when None
            max_list_iter(tlist)
        self.assertEqual(max_list_iter([1, 3, 2, 4, 5, 8, 7, 6]), 8)                # all different, positive numbers
        self.assertEqual(max_list_iter([-2, 7, -5, -4, 3, 1, 100, 3]), 100)         # all different values with negative numbers
        self.assertEqual(max_list_iter([-3, 1.2, 4, 6, -3, 9.5, 33, 40.5, 2]), 40.5)# all different values with floating points
        self.assertEqual(max_list_iter([3, 5, 2, 2, 7, 10, 10]), 10)                # different values repeat number is max
        self.assertEqual(max_list_iter([133, 22, 8, -6, 23.1, 67.2, 23.1, -9]), 133)# max vlaue is the first one
        self.assertEqual(max_list_iter([]), None)                                   # empty list
        self.assertEqual(max_list_iter([3]), 3)                                     # list with 1 value
        self.assertEqual(max_list_iter([-2, -1, 0, 0, 1, 2]), 2)                    # value in the same order
        self.assertEqual(max_list_iter([-5, -3, -8, -100, -30, -5, -4]), -3)        # list with all negatives

    def test_reverse_rec(self):
        # These are the test cases for reverse_rec
        tlist = None
        with self.assertRaises(ValueError):                                 # used to check for exception, when None
            reverse_rec(tlist)
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])                      # Hatalsky test
        self.assertEqual(reverse_rec([]),[])                                # empty list
        self.assertEqual(reverse_rec([1, 1, 1, 1]),[1, 1, 1, 1])            # list with the same values
        self.assertEqual(reverse_rec([-4, -5, 1, 8, 9]), [9, 8, 1, -5, -4]) # list of randoms, arranged
        self.assertEqual(reverse_rec([1.1, 1.2, 1.3, 1.4, 1.5]), [1.5, 1.4, 1.3, 1.2, 1.1])
        self.assertEqual(reverse_rec([3]), [3])                             # one value list
        self.assertEqual(reverse_rec([3, 4]), [4, 3])                       # two value list
        
    def test_bin_search(self):
        # These are the test cases for bin_search
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(7, 1, 9, list_val), 5)                  # same list, different high and low
        self.assertEqual(bin_search(1, 1, 3, list_val), 1)                  # target is the same as the low
        self.assertEqual(bin_search(8, 0, 6, list_val), 6)                  # target is the same index as high
        self.assertEqual(bin_search(3, 4, 8, list_val), None)               # 3 is out of the range of low and high
        self.assertEqual(bin_search(3, 3, 3, list_val), 3)                  # when high = low, and target = low
        self.assertEqual(bin_search(4, 3, 3, list_val), None)               # when high = low and value isn't in there
        self.assertEqual(bin_search(5, 0, 7, list_val), None)               # target isn't in the list, and the case of low > high will act
        self.assertEqual(bin_search(9, low, high, list_val), 7)
        self.assertEqual(bin_search(3, 2, high, list_val), 3)               

        self.assertEqual(bin_search(-2, 4, 9, []), None)                    # empty list

        self.assertEqual(bin_search(-4, 0, 0, [-4]), 0)                     # when len(int_list) = 1, and element is in list
        self.assertEqual(bin_search(2, 0, 0, [-4]), None)                   # when len(int_list) = 1, and element is not in list

        self.assertEqual(bin_search(1, 5, 2, [1, 2, 3, 4]), None)           # when low > high

        tlist = None
        with self.assertRaises(ValueError):                                 # used to check for exception, when None
            bin_search(3, 4, 6, tlist)

if __name__ == "__main__":
        unittest.main()

    
