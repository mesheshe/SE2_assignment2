import unittest
from contrived_func import contrived_func as cf


class tts(unittest.TestCase):

    def test1(self):
        self.assertTrue(cf(125))

    def test2(self):
        self.assertFalse(cf(6))

    def test3(self):
        self.assertTrue(cf(0))

    def test4(self):
        self.assertTrue(cf(80))

    def test5(self):
        self.assertFalse(cf())

    def test6(self):
        self.assertTrue(cf(125))

    def test7(self):
        self.assertTrue(cf(125))


if __name__ == '__main__':
    unittest.main()
