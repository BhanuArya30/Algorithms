import pytest
from p1_minimum_size_subarray_sum import minSubArrLen

def test_valid_inputs():
    assert minSubArrLen([2,3,1,2,4,3],7) == 2
