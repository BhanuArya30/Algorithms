from typing import List

# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target
# Time O(n) | Space O(1) - two pointer
# def pairWithTargetSum(nums:list[int], target) -> list[int]:
#     begin = 0
#     end = len(nums) - 1

#     while begin < end:
#         if nums[begin] + nums[end] == target:
#             return [begin, end]
#         elif nums[begin] + nums[end] > target:
#             end -= 1
#         else:
#             begin += 1

#     return None

# Time O(n) | Space O(n) - with hashmap
# def pairWithTargetSum(nums: list[int], target) -> list[int]:
#     indices_map = {}

#     for idx, num in enumerate(nums):
#         complement = target - num
#         if num not in indices_map:
#             indices_map[complement] = idx
#         else:
#             return [indices_map[num], idx]
    
#     return []


# Time O(n) | Space O(n) - with hashmap - optimized
def pairWithTargetSum(nums: list[int], target) -> list[int]:
    indices_map = {}

    for idx, num in enumerate(nums):
        complement = target - num
        if complement in indices_map:
            return [indices_map[num], idx]
        indices_map[num] = idx
    
    return []

if __name__ == "__main__":
    print(pairWithTargetSum([1, 2, 3, 4, 6], 6))
    # //[1,3]

    # print(pairWithTargetSum([2, 5, 9, 11], 11)) 
    # //[0,2]