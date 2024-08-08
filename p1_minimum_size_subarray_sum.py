from typing import List
#Given an array of positive numbers and a positive number S, find the length of the smallest contiguous subarray whose sum is greater than or equal to S.
#Return 0 if no such subarray exists.

# Time O(n)
def minSubArrLen(nums:List[int], target:int):
    start = 0
    window_sum = 0
    minlength = float('inf')

    for end in range(len(nums)):
        window_sum += nums[end]
        while window_sum >= target:
            minlength = min(minlength, end - start + 1)
            window_sum = window_sum - nums[start]
            start += 1
    
    if minlength == float('inf'):
        return 0
    return minlength


if __name__=="__main__":
    target = 7
    nums = [2,3,1,2,4,3] # 2
    # target = 4
    # nums = [1,4,4] # 3
    # target = 11
    # nums = [1,1,1,1,1,1,1,1]# 0
    print(minSubArrLen(nums, target)) # 2