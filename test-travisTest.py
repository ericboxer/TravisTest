import unittest
import travisTest

class TestTravisTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(travisTest.add(4,5),9)

if __name__ == '__main__':
    unittest.main()