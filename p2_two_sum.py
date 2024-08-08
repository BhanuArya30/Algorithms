from typing import List

# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target
def pairWithTargetSum(nums:list[int], target) -> list[int]:
    begin = 0
    end = len(nums) - 1
    
    while begin < end:
        if nums[begin] + nums[end] == target:
            return [begin, end]
        elif nums[begin] + nums[end] > target:
            end -= 1
        else:
            begin += 1
    
    return None
                    

if __name__=="__main__":
    # print(pairWithTargetSum([1, 2, 3, 4, 6], 6))
    # //[1,3]

    print(pairWithTargetSum([2, 5, 9, 11], 11))
    # //[0,2]