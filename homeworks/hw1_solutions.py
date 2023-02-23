# Write a function "repeat(a, x)" which takes a character variable a and
# a number x and outputs a string of the character a repeated x times.
#
# Examples:
# repeat('d', 3) --> 'ddd'
# repeat('z', 2) --> 'zz'
def repeat(a, x):
    s = ''
    while x > 0:
        s += a
        x -= 1
    return s


# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday or we're on vacation.
# Return True if we sleep in.
#
# Examples:
# sleep_in(False, False) --> True (because it's not a weekday)
# sleep_in(True, False) --> False (because it's a weekday, and we're not on vacation)
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    return False


# Given an int n, return True if it is within 10 of 100 or a multiple of 100 like 200, 300...
# Note: abs(num) computes the absolute value of a number.
#
# Examples:
# near_hundred(97) --> True
# near_hundred(89) --> False
# near_hundred(398) --> True
# near_hundred(456) --> False
def near_hundred(x):
    if x < 90:
        return False
    y = abs(x % 100 - 100)
    if y <= 10 or y >= 90:
        return True
    return False


# Given a non-empty string s and an int n, return a new string where the char at
# index n has been removed.
# The value of n will be a valid index of a char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).
#
# Examples:
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'
def missing_char(s, x):
    return s[:x] + s[x+1:]

# Given a non-empty string s, return a new string which is the reverse of s.
#
# Examples:
#
# reverse_string('hello') --> 'olleh'


def reverse_string(s):
    val = ""
    for i in range(len(s)):
        val += s[-i-1]
    return val


# Given a string and a non-negative int n, we'll say that the front of the string is
# the first 3 chars, or whatever is there if the string is less than length 3.
# Return n copies of the front
#
# Examples:
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Chocolate', 3) → 'ChoChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'
def front_times(s, x):
    front = s[:3]
    return front*x


# Given 2 strings, a and b, return the number of the positions where they contain the
# same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa",
# and "az" substrings appear in the same place in both strings.
# Example
# string_match('xxcaazz', 'xxbaaz') → 3
# string_match('abc', 'abc') → 2
# string_match('abc', 'axc') → 0
def string_match(a, b):
    count = 0
    for i in range(len(a) - 1):
        if a[i] == b[i] and a[i+1] == b[i+1]:
            count += 1
    return count


# Given two lists of integers of the same length, return a new list containing
# the element-wise sum of the two lists.
#
# sum_lists([1, 2, 3], [4, 5, 6]) --> [5, 7, 9]
# sum_lists([1, 2], [2, 1]) --> [3, 3]
#
def sum_lists(a, b):
    L = []
    for i in range(len(a)):
        L.append(a[i] + b[i])
    return L


# Given an int array, return how many 2s and 3s it contains.
#
# num23([1, 2, 5]) → 1
# num23([1, 3, 4, 3, 2]) -> 3
def num23(l):
    count = 0
    for i in l:
        if i == 2 or i == 3:
            count += 1
    return count


# Return the number of times that the string "code" appears anywhere in the
# given string, except we'll accept any letter for the 'd', so "cope" and "cooe"
# count.
# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2
def count_code(s):
    count = 0
    for i in range(len(s)-3):
        if s[i] == 'c' and s[i+1] == 'o' and s[i+3] == 'e':
            count += 1
    return count
