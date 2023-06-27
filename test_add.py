import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_integers(self):
        result = add(1, 2)
        self.assertEqual(result, 3)

    def test_add_floats(self):
        result = add(0.1, 0.2)
        self.assertAlmostEqual(result, 0.3)

    def test_add_strings(self):
        result = add('hello', 'world')
        self.assertEqual(result, 'helloworld')

if __name__ == '__main__':
    unittest.main()
