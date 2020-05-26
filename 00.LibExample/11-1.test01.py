import unittest

class TestSample(unittest.TestCase):
    def test_upper(self):
        # self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual('foo'.upper(), 'Foo')


if __name__ == '__main__':
    unittest.main()