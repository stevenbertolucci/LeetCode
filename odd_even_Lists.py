# Pull request 4
def get_val_index(arr, val):
    """Searches arr for every instance the val and returns the index if found, otherwise None"""

    # Initialize result array to hold the index(s)
    result = []
    for i in range(len(arr)):
        # If val exists save the index
        if arr[i] == val:
            result.append(i)
    # Return the results
    return result if result is not None else None


array = [9, 3, 5, 1, 7, 4, 5, 6, 4, 2, 3]
result = get_val_index(array, 4)
print(result)




