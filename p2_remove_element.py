# Given an unsorted array of numbers and a target key, 
# remove all instances of key in-place and return the new length of the array.

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    write_idx = 0

    for read_idx in range(len(nums)):
        if nums[read_idx] != val:
            nums[write_idx] = nums[read_idx]
            write_idx += 1

    return write_idx