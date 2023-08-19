from unittest import TestCase
from compute_stats_refactor import (
    average, count, maximum, minimum, read_ints, summation
)


class TestComputeStats(TestCase):

    def test_read_ints(self):
        numbers = read_ints()
        self.assertGreater(len(numbers), 0)

    def test_count(self):
        numbers = read_ints()
        return self.assertEqual(len(numbers), count())

    def test_summation(self):
        numbers = read_ints()
        result = sum(numbers)
        return self.assertEqual(result, summation())

    def test_average(self):
        c = count()
        s = summation()
        return self.assertEqual(s/c, average())

    def test_minimum(self):
        m = min(read_ints())
        return self.assertEqual(m, minimum())

    def test_maximum(self):
        m = max(read_ints())
        return self.assertEqual(m, maximum())
