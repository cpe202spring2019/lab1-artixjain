import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")
  
        loc = Location("California", 32.5, 2)
        self.assertEqual(repr(loc),"Location('California', 32.5, 2)")  

        loc1 = Location("California", 32.5, 2)
        loc2 = Location("California", 32.5, 2)

        def test_eq(self):
        	loc1 = Location("California", 32.5, 2)
        	loc2 = Location("California", 32.5, 2)
        	loc3 = Location("California", 32.5, 3)
        	loc4 = Location("Campbell", 43.9, 34.1)
        	
        	self.assertTrue(loc1 == loc2)
        	self.assertFalse(loc2 == loc3)
        	self.assertFalse(loc4 == loc1)

if __name__ == "__main__":
        unittest.main()
