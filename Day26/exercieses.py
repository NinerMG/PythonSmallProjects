# Squaring Numbers
# You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.
#
# e.g.
#
# 4 * 4 = 16
#
# 4 squared equals 16.
#
# **DO NOT** modify the List numbers directly. Try to use List Comprehension instead of a Loop.
#
# Target Output
#
# [1, 1, 4, 9, 25, 64, 169, 441, 1156, 3025]
import math

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [int(math.pow(n,2)) for n in numbers]
print(squared_numbers)

# Filtering Even Numbers
# In this list comprehension exercise you will practice using list comprehension to filter out the even numbers from a series of numbers.
#
# First, use list comprehension to convert the list_of_strings to a list of integers called numbers.
#
# Then use list comprehension again to create a new list called result.
#
# This new list should only contain the even numbers from the list numbers.
#
# Again, try to use Python's List Comprehension instead of a Loop.

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 ==0]
print(result)

