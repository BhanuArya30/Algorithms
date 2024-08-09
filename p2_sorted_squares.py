from typing import List

# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

# # Time O(nlogn) | Space O(n)
# def sortedSquares(self, nums: List[int]) -> List[int]:
#     return sorted([n**2 for n in nums])

# Time O(n) | Space O(n)
def sortedSquares(self, nums: List[int]) -> List[int]:
    l = 0
    r = len(nums) - 1
    result = [0] * len(nums)

    for idx in reversed(range(len(nums))):
        if abs(nums[l]) > abs(nums[r]):
            result[idx] = nums[l] ** 2
            l += 1
        else:
            result[idx] = nums[r] ** 2
            r -= 1

    return result
