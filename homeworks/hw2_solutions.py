"""
1. Write a function that takes a list of integers as input and returns a new
   list containing only the even integers from the input list.

Example:
input: [1, 2, 3, 4, 5, 6]
output: [2, 4, 6]

input: [7, 8, 9]
output: [8]
"""


import math


def filter_even_numbers(l):
    even_numbers = []
    for i in l:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


"""
2. Write a function that takes a list of integers as input and returns the
   largest difference between any two integers in the list.

Example:
input: [1, 6, 2, 3, 5]
output: 5  # largest difference is between 1 and 6

input: [9, 3, 1, 5]
output: 8  # largest difference is between 9 and 1
"""


def largest_difference(l):
    max_difference = 0
    for i in l:
        for j in l:
            if abs(i - j) > max_difference:
                max_difference = abs(i - j)
    return max_difference


"""
3. Write a function that takes a string as input and returns True if the string
   is a palindrome (a word or phrase that is spelled the same way forwards and
   backwards).

Example:
input: "racecar"
output: True

input: "hello"
output: False
"""


def is_palindrome(s):
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False
    return True


"""
4. Write a function that takes a list of strings as input and returns the longest string in the list.

Example:
input: ["hello", "world", "python"]
output: "python"

input: ["a", "bb", "ccc"]
output: "ccc"
"""


def longest_string(l):
    longest_string = ''
    for s in l:
        if len(s) > len(longest_string):
            longest_string = s
    return longest_string


"""
5. Write a function that takes a list of integers and a number n as input and
   returns the n-th largest integer in the list. If n is 1, it means the largest
   element. If n is 2, it means the 2nd largest element. If n is 3, it means the
   3rd largest element, etc...

Example:
input: [9, 4, 5, 8] and n = 3
output: 5

input: [3, 2, 7] and n = 2 
output: 3
"""


def nth_largest(l, n):
    val = 0
    for i in range(n):
        val = max(l)
        l.remove(val)
    return val


"""
6. Write a function that takes two dictionaries as input and returns a new
   dictionary that contains all the keys and values from the two input
   dictionaries.
If a key is present in both dictionaries, the value from the second dictionary
should be used.

Example:
input: {"a": 1, "b": 2}, {"c": 3, "b": 4}
output: {"a": 1, "b": 4, "c": 3}

input: {"x": 10, "y": 20}, {"y": 30, "z": 40}
output: {"x": 10, "y": 30, "z": 40}
"""


def merge_dictionaries(d1, d2):
    for key in d2.keys():
        d1[key] = d2[key]
    return d1


"""
7. Write a function that takes a string as input and returns a dictionary
   containing the frequency of each character in the string.

Example:
Input: "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
"""


def get_character_frequency(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


"""
8. Write a class that represents a bank account with a balance and methods to
   deposit and withdraw money from the account.

Example:
acct = BankAccount(1000)  # creates an account with initial balance of 1000
acct.deposit(500)  # adds 500 to the account balance
acct.withdraw(200)  # subtracts 200 from the account balance
acct.balance()  # returns the current balance (should be 1300)
"""


class BankAccount:
    bal = 0

    def __init__(self, balance):
        self.bal = balance

    def deposit(self, amount):
        self.bal += amount

    def withdraw(self, amount):
        self.bal -= amount

    def balance(self):
        return self.bal


"""
9. Write a class that represents a point in 2D space with x and y coordinates,
   and methods to calculate the distance between two points.

Example:
p1 = Point(0, 0)  # creates a point at (0, 0)
p2 = Point(3, 4)  # creates a point at (3, 4)
p1.distance_to(p2)  # returns 5.0 (distance between points p1 and p2)
"""


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, p):
        return math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)


"""
10. Create a shopping cart class that allows a user to add items to their cart,
    remove items from their cart, and calculate the total cost of all items in
    the cart. The class should keep track of the quantity of each item in the cart.

Example:
cart = ShoppingCart()
cart.register_item("apple", 10) # set the cost of an apple to 10 dollars
cart.register_item("banana", 5) # set the cost of a banana to 5 dollars
cart.add_item("apple", 2)  # adds 2 apples to the cart
cart.add_item("banana", 10)  # adds 10 bananas to the cart
cart.remove_item("banana", 1)  # removes 1 banana from the cart
cart.total_cost()  # returns 65 because there are 9 bananas and 2 apples in cart.
"""


class ShoppingCart:
    items = {}
    prices = {}

    def register_item(self, item, price):
        self.prices[item] = price

    def add_item(self, item, amount):
        if item in self.items:
            self.items[item] += amount
        else:
            self.items[item] = amount

    def remove_item(self, item):
        self.items[item] -= 1
        if self.items[item] == 0:
            self.items.pop(item)

    def total_cost(self):
        total = 0
        for item in self.items:
            total += self.items[item] * self.prices[item]
        return total
