# ToDo - Finish implementing binary search. As of right now, this file is incomplete ********

def binary_search(arr, low, high, x):

    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, low, high + 1, x)

        else:
            return binary_search(arr, low, high - 1, x)

    else:
        return -1


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 12, 20]
    x = 5

    result = binary_search(array, 0, len(array) - 1, x)
    if result != -1:
        print("The number exists in the array at index: ", str(result))
    else:
        print("It does not exist in the array.")
