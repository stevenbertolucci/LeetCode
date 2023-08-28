# Author: Steven Bertolucci
# Date: 8.27.23
# File Description: This file generates random list of 100 elements (any positive integers from 1-100 and then the
#                   program will then choose a random number between 1-8 that will be used to multiply the value of the
#                   index.

import random


def randomizeTheArray():
    array = [0 for i in range(100)]
    for i in range(len(array)):
        array[i] = random.randrange(1, 101)
    return array


def sortArray(array):

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] >= array[j]:
                array[i], array[j] = array[j], array[i]
    return array


def multiplyTheArray(array):
    value = [0 for i in range(len(array))]
    for i in range(len(array)):
        value[i] = random.randrange(1, 9)
        array[i] = array[i] * value[i]
    return array, value


if __name__ == "__main__":

    randomArray = randomizeTheArray()
    print("The random generated array is: \t", randomArray)
    print("The sorted array is: \t\t\t", sortArray(randomArray))
    result, number = multiplyTheArray(randomArray)
    print("The value to be multiplied: \t", number, "\nThe multiplied array is: \t\t", result)
