import unittest
from grid import GridMapProcessor


class TestMagnifyFunction(unittest.TestCase):

    def test_magnify_by_2(self):
        input_grid = [
            [0, 0, 2, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        processor = GridMapProcessor.from_grid(input_grid)
        expected_output = [
            [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        self.assertEqual(processor.magnify(2).grid, expected_output)

    def test_magnify_by_3(self):
        input_grid = [
            [0, 2, 0],
            [0, 0, 0],
            [0, 0, 2]
        ]
        processor = GridMapProcessor.from_grid(input_grid)
        expected_output = [
            [0, 0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 2, 2, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 2, 2, 2]
        ]
        self.assertEqual(processor.magnify(3).grid, expected_output)

    def test_magnify_single_element(self):
        input_grid = [[1]]
        processor = GridMapProcessor.from_grid(input_grid)
        expected_output = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(processor.magnify(2).grid, expected_output)

    def test_magnify_size_1(self):
        input_grid = [
            [0, 2, 0],
            [0, 1, 0],
            [0, 0, 2]
        ]
        processor = GridMapProcessor.from_grid(input_grid)
        expected_output = [
            [0, 2, 0],
            [0, 1, 0],
            [0, 0, 2]
        ]
        self.assertEqual(processor.magnify(1).grid, expected_output)


if __name__ == '__main__':
    unittest.main()
