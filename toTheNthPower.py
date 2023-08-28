# Author: Steven Bertolucci
# Date: 8.27.23
# File Description: This file prints the unsorted array, sorted array, and then the array whose index is
#                   used as the power to multiply that index value. For example, if index #6 has the value
#                   of 2, then this program will calculate that index as 2^6. If index #7 has the value
#                   of 8, then this program will calculate that index as 8^7 and so on.

def toTheNthPower(array):
    starting_Index = 1
    temp = [0]

    for i in range(len(array)):
        if i == 0:
            array[i] = array[i]
            starting_Index += 1
        else:
            temp[0] = array[i]
            while starting_Index != 1:
                array[i] = array[i] * temp[0]
                starting_Index -= 1
            starting_Index = i + 1
            starting_Index += 1

    return array


def sortArray(array):

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] >= array[j]:
                array[i], array[j] = array[j], array[i]
    return array


if __name__ == "__main__":

    theArray = [2, 3, 4, 1, 8, 3, 2, 8, 2, 5]

    print("The unsorted array is: ", theArray)
    print("The sorted array is: ", sortArray(theArray))
    print("The nth Power of the array is: ", toTheNthPower(theArray))
