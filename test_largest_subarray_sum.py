import pytest
from largest_subarray_length_k import largestSubarraySum

def test_valid_input():
    assert largestSubarraySum([1, 2, 3, 4, 5], 3) == 12
    assert largestSubarraySum([-1, -2, -3, -4, -5], 2) == -3
    assert largestSubarraySum([2, 3, -1, 4, 5], 3) == 8

def test_invalid_input():
    with pytest.raises(ValueError):
        largestSubarraySum([1, 2, 3], 0)
    with pytest.raises(ValueError):
        largestSubarraySum([1, 2, 3], 5)

def test_edge_cases():
    assert largestSubarraySum([1], 1) == 1
    assert largestSubarraySum([-1], 1) == -1