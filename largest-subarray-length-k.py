from typing import List

# Given an array of positive numbers and a positive number K, find the maximum sum of any contiguous subarray of size K.
def largestSubarraySum(nums:List[int], k:int) -> int:
    '''
    Find the maximum sum of contigous subarray of length k in nums.
    '''
    if k <= 0:
        raise ValueError("k cannot be less than or equal to zero.")
    n = len(nums)
    if k > n:
        raise ValueError("k cannot be greater than length of array.")

    new_sum = sum(nums[:k])
    max_sum = new_sum

    for idx in range(1, n - k + 1):        
        new_sum = new_sum - nums[idx - 1] + nums[idx + k - 1]
        max_sum = max(max_sum, new_sum)

    return max_sum


if __name__ == "__main__":
    # nums = [2, 1, 5, 1, 3, 2]
    # k = 3 # 9
    # nums = [2, 3, 4, 1, 5]
    # k = 2
    nums = [1, 2, 3, 4, 5]
    k = 5
    print(largestSubarraySum(nums, k))
