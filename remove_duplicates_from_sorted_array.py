from typing import List

# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; 
# after removing the duplicates in-place return the length of the subarray that has no duplicate in it.

# Time O(n) | Space O(1)
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    unique_idx = 0

    for idx in range(1, len(nums)):
        if nums[idx] != nums[idx - 1]:
            unique_idx += 1
            nums[unique_idx] = nums[idx]
    
    return unique_idx + 1


if __name__ == "__main__":
    # Example usage:
    nums = [0, 0, 1, 1, 2, 2, 3, 3, 4]
    length = removeDuplicates(nums)
    print(length)  # Output should be 5
    print(nums[:length])  # Output should be [0, 1, 2, 3, 4]