import unittest
from grid import GridMapProcessor


class TestMagnifyFunction(unittest.TestCase):

    def test_magnify_by_2(self):
        input_grid = [
            ['L', 'L', 'O', 'L', 'L'],
            ['L', 'L', 'O', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L'],
            ['L', 'L', 'L', 'L', 'L']
        ]
        processor = GridMapProcessor.from_grid(input_grid)
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
        self.assertEqual(processor.magnify(2), expected_output)

    def test_magnify_by_3(self):
        input_grid = [
            ['L', 'O', 'L'],
            ['L', 'L', 'L'],
            ['L', 'L', 'O']
        ]
        processor = GridMapProcessor.from_grid(input_grid)
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
        self.assertEqual(processor.magnify(3), expected_output)

    def test_magnify_single_element(self):
        input_grid = [['S']]
        processor = GridMapProcessor.from_grid(input_grid)
        expected_output = [
            ['S', 'S'],
            ['S', 'S']
        ]
        self.assertEqual(processor.magnify(2), expected_output)

    def test_magnify_size_1(self):
        input_grid = [
            ['L', 'O', 'L'],
            ['L', 'S', 'L'],
            ['L', 'L', 'O']
        ]
        processor = GridMapProcessor.from_grid(input_grid)
        expected_output = [
            ['L', 'O', 'L'],
            ['L', 'S', 'L'],
            ['L', 'L', 'O']
        ]
        self.assertEqual(processor.magnify(1), expected_output)


if __name__ == '__main__':
    unittest.main()
