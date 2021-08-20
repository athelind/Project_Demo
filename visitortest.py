import unittest
from demo import Visitors

class testMath(unittest.TestCase):

    def testMYVisitors(self):
        visitor = Visitors()
        result = Visitors.getMalaysia2000VisitorCount(visitor)
        self.assertEqual(result, 564790)