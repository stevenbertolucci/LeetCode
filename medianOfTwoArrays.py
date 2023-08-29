# Author: Steven Bertolucci
# Date: 8.29.23
# LeetCode Problem List #4: Median of Two Sorted Arrays
# Difficulty: Hard
# File Description: Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of
# the two sorted arrays. The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1, nums2):

    print("nums1: ", nums1, "\t\tnums2: ", nums2)
    # Combine the two arrays
    for i in range(len(nums2)):
        nums1.append(nums2[i])

    # Sort the array
    nums1.sort()
    print("The sorted array is: \t\t\t\t\t\t", nums1)

    # Is the number of indices even?
    if len(nums1) % 2 == 0:
        midpoint = len(nums1) // 2
        previous = (len(nums1) // 2) - 1
        median = (nums1[midpoint] + nums1[previous]) / 2
    else:
        midpoint = len(nums1) / 2
        median = nums1[midpoint]

    return median


if __name__ == "__main__":

    array1, array2 = [2, 1, 8, 11], [3, 4, 5, 2]

    print("The median of the two sorted arrays is: \t", findMedianSortedArrays(array1, array2))
