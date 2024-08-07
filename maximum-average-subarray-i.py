from typing import List
from utils import timing_decorator


# You are given an integer array nums consisting of n elements, and an integer k.

# Time O(n * k)
# @timing_decorator
# def findMaxAverage(nums: List[int], k: int) -> float:
#     n = len(nums)
#     assert k <= n
#     max_average = 0
#     for idx in range(0, n - k + 1):
#         current_average = sum(nums[idx : idx + k]) / k
#         max_average = max(max_average, current_average)
#     return max_average


# Time O(n)
# @timing_decorator
# def findMaxAverage(nums: List[int], k: int) -> float:
#     n = len(nums)
#     assert k <= n
#     current_sum = 0
#     current_average = 0
#     max_average = 0
#     for idx in range(0, n-k+1):
#         if idx == 0:
#             current_sum = sum(nums[idx: idx+k])
#         else:
#             current_sum = current_sum + nums[idx+k-1] - nums[idx-1]
#         current_average = current_sum / k
#         max_average = max(max_average, current_average)
#     return max_average


# Time O(n) - optimized code
@timing_decorator
def findMaxAverage(nums: List[int], k: int) -> float:
    n = len(nums)
    if k > n:
        raise ValueError("k cannot be greater than n")

    current_sum = sum(nums[:k])
    max_average = current_sum / k

    for idx in range(1, n - k + 1):
        current_sum = current_sum + nums[idx + k - 1] - nums[idx - 1]
        max_average = max(max_average, current_sum / k)

    return max_average


if __name__ == "__main__":
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(findMaxAverage(nums, k))
