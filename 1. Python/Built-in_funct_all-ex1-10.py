# Built-in funct ex1-10

# Bulit-in funct ex1-2

alpha = "Hello World!"

count_alpha = len(alpha)
print(count_alpha)

count_float = float(count_alpha)

# Bulit-in funct ex3

import math

pi = math.pi
round_pi = round(pi, 2)
print(round_pi)


# Built-in funct ex4

text = "Hello world!"
reversed_text = list(text[::-1])
print(reversed_text)


# Built-in funct ex5

age = input("Enter your age : ")
print(age)
print(type(age))


# Built-in funct ex6-7-8-9

num = [2, 8, 1, 4, 6, 3, 7]

sorted_num = sorted(num)
sum_of_list = sum(sorted_num)
min_value = min(num)
max_value = max(num)


# Built-in funct ex10

calc = "1 + 2"
string_interpret = eval(calc)
print(string_interpret)


import unittest


class TestNotebook(unittest.TestCase):
    def test_count_alpha(self):
        self.assertEqual(count_alpha, 12)

    def test_count_float(self):
        self.assertEqual(type(count_float), float)

    def test_pi(self):
        self.assertEqual(3.14, round_pi)

    def test_reversed(self):
        self.assertEqual(
            reversed_text, ["!", "d", "l", "r", "o", "w", " ", "o", "l", "l", "e", "H"]
        )

    def test_age(self):
        self.assertEqual(type(age), str)

    def test_sorted(self):
        self.assertEqual(sorted_num, [1, 2, 3, 4, 6, 7, 8])

    def test_sum(self):
        self.assertEqual(sum_of_list, 31)

    def test_min(self):
        self.assertEqual(min_value, 1)

    def test_max(self):
        self.assertEqual(max_value, 8)

    def test_interpret(self):
        self.assertEqual(string_interpret, 3)


unittest.main(argv=[""], verbosity=2, exit=False)