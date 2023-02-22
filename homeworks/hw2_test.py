import unittest

from hw2 import (
    BankAccount,
    Point,
    ShoppingCart,
    filter_even_numbers,
    get_character_frequency,
    is_palindrome,
    largest_difference,
    longest_string,
    merge_dictionaries,
    nth_largest,
)


class Homework2Test(unittest.TestCase):

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(filter_even_numbers([7, 8, 9]), [8])

    def test_largest_difference(self):
        self.assertEqual(largest_difference([1, 6, 2, 3, 5]), 5)
        self.assertEqual(largest_difference([9, 3, 1, 5]), 8)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("a"))

    def test_longest_string(self):
        self.assertEqual(longest_string(["hello", "world", "python"]), "python")
        self.assertEqual(longest_string(["a", "bb", "ccc"]), "ccc")

    def test_nth_largest(self):
        self.assertEqual(nth_largest([9, 4, 5, 8], 3), 5)
        self.assertEqual(nth_largest([3, 2, 7], 2), 3)

    def test_merge_dictionaries(self):
        self.assertEqual(
            merge_dictionaries({"a": 1, "b": 2},
                               {"c": 3, "b": 4}),
            {"a": 1, "b": 4, "c": 3})
        self.assertEqual(
            merge_dictionaries({"x": 10, "y": 20},
                               {"y": 30, "z": 40}),
            {"x": 10, "y": 30, "z": 40})

    def test_get_character_frequency(self):
        self.assertEqual(
            get_character_frequency("hello"),
            {'h': 1, 'e': 1, 'l': 2, 'o': 1})

    def test_bank_account(self):
        acct = BankAccount(1000)
        acct.deposit(500)
        acct.withdraw(200)
        self.assertEqual(acct.balance(), 1300)

    def test_point(self):
        p1 = Point(0, 0)
        p2 = Point(3, 4)
        self.assertEqual(p1.distance_to(p2), 5.0)

    def test_shopping_cart(self):
        cart = ShoppingCart()
        cart.register_item("apple", 10)
        cart.register_item("banana", 5)
        cart.add_item("apple", 2)
        cart.add_item("banana", 10)
        cart.remove_item("banana")
        self.assertEqual(cart.total_cost(), 65)


if __name__ == '__main__':
    unittest.main()
