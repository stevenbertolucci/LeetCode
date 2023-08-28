def doubleOfArray(array):

    for i in range(len(array)):
        array[i] = array[i] * array[i]

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
    print("The square of the array is: ", doubleOfArray(theArray))
