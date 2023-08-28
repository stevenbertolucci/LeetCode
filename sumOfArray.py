def sumOfArray(array):
    total = [0]

    for i in range(len(array)):
        total[0] += array[i]

    return total


if __name__ == "__main__":

    theArray = [2, 3, 4, 1, 8, 3, 2, 8, 2, 5]
    result = sumOfArray(theArray)
    print("The sum of the array is: ", result)
