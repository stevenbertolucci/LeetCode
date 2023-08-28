# Author: Steven Bertolucci
# Date: 7.16.23
# File Description: THis file takes in an array and sorts it


# ---------------------------------------------------------
#     This function sorts the array in ascending order
# ---------------------------------------------------------
def sortAscending(givenArray):

    for i in range(len(givenArray)):
        for j in range(i + 1, len(givenArray)):
            if givenArray[i] > givenArray[j]:
                givenArray[i], givenArray[j] = givenArray[j], givenArray[i]
    return givenArray


# ---------------------------------------------------------
#    This function sorts the array in descending order
# ---------------------------------------------------------
def sortDescending(givenArray):

    for i in range(len(givenArray)):
        for j in range(i + 1, len(givenArray)):
            if givenArray[i] < givenArray[j]:
                givenArray[i], givenArray[j] = givenArray[j], givenArray[i]
    return givenArray


if __name__ == "__main__":

    # Test one
    array = [4, 3, 8, 3, 1, 9, 0]
    result = sortAscending(array)
    print("The sorted, ascending array is: ", result)

    # Test two
    array = [3, 3, 2, 1, 3]
    result = sortAscending(array)
    print("The sorted, ascending array is: ", result)

    # Test three
    array = [0, -1, 123, -7, -3]
    result = sortAscending(array)
    print("The sorted, ascending array is: ", result)

    print("\n")

    # Test four
    array = [4, 3, 8, 3, 1, 9, 0]
    result = sortDescending(array)
    print("The sorted, descending array is: ", result)

    # Test Five
    array = [3, 3, 2, 1, 3]
    result = sortDescending(array)
    print("The sorted, descending array is: ", result)

    # Test Six
    array = [0, -1, 123, -7, -3]
    result = sortDescending(array)
    print("The sorted, descending array is: ", result)
