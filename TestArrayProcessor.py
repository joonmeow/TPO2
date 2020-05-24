import unittest
from ProdactionCode.ArrayProcessor import ArrayProcessor


class TestArrayProcessor(unittest.TestCase):
    def setUp(self):
        self.arrayProcessor = ArrayProcessor()
        self.array = [-12, -23, 0, -4, 2, 55, -23, -4, 55, 2, 3, 2, 12]
        self.resultArray = [55, 23, 12, 4, 3, 2, 0]

    def test_sort_and_filter(self):
        result = self.arrayProcessor.sortAndFilter(self.array)
        self.assertEqual(result, self.resultArray)
