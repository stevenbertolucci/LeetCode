# Author: Steven Bertolucci
# Date: 8.29.23
# LeetCode Problem List #7: Reverse Integer
# Difficulty: Medium
# File Description: Given a signed 32-bit integer x, return x with its digits reversed.
#                   If reversing x causes the value to go outside the signed 32-bit integer
#                   range [-2^31, 2^31 - 1], then return 0.

# *********************************************************************************************************
#          NOTE: reverse() function still needs boundary edge case implementations for negative numbers
#          and positive numbers in the signed 32-bit range
# *********************************************************************************************************
import random


def reverse(x):

    reversed_num = 0

    while x != 0:
        number = x % 10
        reversed_num = reversed_num * 10 + number
        x //= 10

    return reversed_num


if __name__ == "__main__":

    value = random.randrange(0, 300000)

    print("The integer is: \t\t ", value, "\nThe reversed integer is: ", reverse(value))
