import unittest

from grid import magnify


class TestMagnifyFunction(unittest.TestCase):

    def test_magnify_by_2(self):
        input_grid = [
            ['L', 'L', 'O', 'L', 'L'],
            ['L', 'L', 'O', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L']
        ]
        expected_output = [
            ['L', 'L', 'L', 'L', 'O', 'O', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'O', 'O', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'O', 'O', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'O', 'O', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']
        ]
        self.assertEqual(magnify(input_grid, 2), expected_output)

    def test_magnify_by_3(self):
        input_grid = [
            ['L', 'O', 'L'],
            ['L', 'L', 'L'],
            ['L', 'L', 'O']
        ]
        expected_output = [
            ['L', 'L', 'L', 'O', 'O', 'O', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'O', 'O', 'O', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'O', 'O', 'O', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'O', 'O', 'O'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'O', 'O', 'O'],
            ['L', 'L', 'L', 'L', 'L', 'L', 'O', 'O', 'O']
        ]
        self.assertEqual(magnify(input_grid, 3), expected_output)

    def test_magnify_empty_grid(self):
        input_grid = []
        expected_output = []
        self.assertEqual(magnify(input_grid, 2), expected_output)

    def test_magnify_single_element(self):
        input_grid = [['S']]
        expected_output = [
            ['S', 'S'],
            ['S', 'S']
        ]
        self.assertEqual(magnify(input_grid, 2), expected_output)

    def test_magnify_size_1(self):
        input_grid = [
            ['L', 'O', 'L'],
            ['L', 'S', 'L'],
            ['L', 'L', 'O']
        ]
        expected_output = [
            ['L', 'O', 'L'],
            ['L', 'S', 'L'],
            ['L', 'L', 'O']
        ]
        self.assertEqual(magnify(input_grid, 1), expected_output)


if __name__ == '__main__':
    unittest.main()
