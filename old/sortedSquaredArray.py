# # Time O(n) | Space O(n)
# def sortedSquaredArray(array):
#     n = len(array)
#     i, j = 0, n - 1
#     result = [0] * n
#     for idx in range(n-1, -1, -1):
#         lt_sq = array[i]**2
#         rt_sq = array[j]**2
#         if lt_sq >= rt_sq:
#             result[idx] = lt_sq
#             i += 1
#         else:
#             result[idx] = rt_sq
#             j -= 1
#     return result


# Time O(nlogn) | Space O(n)
def sortedSquaredArray(array):
    """
    function to return squares of sorted array
    >>> sortedSquaredArray([1, 2, 3, 4, 5, 6])
    [1, 4, 9, 16, 25, 36]
    """
    return sorted([num**2 for num in array])


#  Time O(n) | Space O(n)
def sortedSquaredArray(array):
    """
    function to return squares of sorted array
    >>> sortedSquaredArray([1, 2, 3, 4, 5, 6])
    [1, 4, 9, 16, 25, 36]
    """
    n = len(array)
    result = [0] * n
    left = 0
    right = n - 1
    for i in range(n - 1, -1, -1):
        if array[left] ** 2 >= array[right] ** 2:
            result[i] = array[left] ** 2
            left += 1
        else:
            result[i] = array[right] ** 2
            right -= 1
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
