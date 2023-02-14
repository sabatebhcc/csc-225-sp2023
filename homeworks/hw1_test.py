import unittest

from hw1 import *


class Homework1Test(unittest.TestCase):

    def test_repeat(self):
        self.assertEqual(repeat('a', 3), 'aaa')
        self.assertEqual(repeat('x', 10), 'xxxxxxxxxx')
        self.assertEqual(repeat('z', 0), '')
        self.assertEqual(repeat('i', -1), '')

    def test_sleep_in(self):
        self.assertTrue(sleep_in(False, True))
        self.assertTrue(sleep_in(False, False))
        self.assertTrue(sleep_in(True, True))
        self.assertFalse(sleep_in(True, False))

    def test_near_hundred(self):
        self.assertTrue(near_hundred(99))
        self.assertTrue(near_hundred(90))
        self.assertFalse(near_hundred(89))
        self.assertTrue(near_hundred(499))
        self.assertTrue(near_hundred(490))
        self.assertFalse(near_hundred(489))
        self.assertTrue(near_hundred(1199))
        self.assertTrue(near_hundred(1290))
        self.assertFalse(near_hundred(1489))
        self.assertFalse(near_hundred(9))
        self.assertFalse(near_hundred(5))
        self.assertTrue(near_hundred(101))

    def test_missing_char(self):
        self.assertEqual(missing_char('hello', 3), 'helo')
        self.assertEqual(missing_char('shalom', 1), 'salom')

    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('why are we here'), 'ereh ew era yhw')
        self.assertEqual(reverse_string('i'), 'i')
        self.assertEqual(reverse_string(''), '')

    def test_front_times(self):
        self.assertEqual(front_times('Chocolate', 2), 'ChoCho')
        self.assertEqual(front_times('Triple', 3), 'TriTriTri')
        self.assertEqual(front_times('Ab', 4), 'AbAbAbAb')
        self.assertEqual(front_times('s', 2), 'ss')
        self.assertEqual(front_times('', 10), '')

    def test_string_match(self):
        self.assertEqual(string_match('xxcaazz', 'xxbaaz'), 3)
        self.assertEqual(string_match('abc', 'abc'), 2)
        self.assertEqual(string_match('abc', 'axc'), 0)

    def test_sum_lists(self):
        self.assertEquals(sum_lists([1, 2, 3], [4, 5, 6]), [5, 7, 9])
        self.assertEquals(sum_lists([1, 3], [2, 5]), [3, 8])
        self.assertEquals(sum_lists([[0], [1]]), [1])
        self.assertEquals(sum_lists([], []), [])
        self.assertEquals(sum_lists([-1, 0], [1, 0]), [0, 0])

    def test_num23(self):
        self.assertEquals(num23([1]), 0)
        self.assertEquals(num23([2, 4, 3]), 2)
        self.assertEquals(num23([0, 1, 2, 3, 4, 5, 3, 3, 2]), 5)

    def test_count_code(self):
        self.assertEquals(count_code('aaacodebbb'), 1)
        self.assertEquals(count_code('codexxcode'), 2)
        self.assertEquals(count_code('cozexxcope'), 2)


if __name__ == '__main__':
    unittest.main()
