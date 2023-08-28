# ------------------------------------------------------------------------------------------------------
#   Description:
#   Given an array of integers nums and an integer target, return indices of the two numbers
#   such that they add up to target. You may assume that each input would have exactly one solution,
#   and you may not use the same element twice. You can return the answer in any order.
# ------------------------------------------------------------------------------------------------------


def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    num1 = 0
    num2 = 0

    for i in range(len(nums)):

        if i == len(nums) - 1:
            return None

        num1 = nums[i]
        num2 = nums[i + 1]

        if num1 + num2 == target:
            return [i, i + 1]
        else:
            for i in range(len(nums)):
                i += 1

                if i == len(nums) - 1:
                    return None

                nums2 = nums[i + 1]

                if num1 + num2 == target:
                    return [i - 1, i + 1]
                i -= 1


array = [2, 3, 4, 1, 8, 3, 2, 8, 2, 5]
total = 12
