# Time O(n) | Space O(n)
def sortedSquaredArray(array):
    n = len(array)
    i, j = 0, n - 1
    result = [0] * n
    for idx in range(n-1, -1, -1):
        lt_sq = array[i]**2
        rt_sq = array[j]**2
        if lt_sq >= rt_sq:
            result[idx] = lt_sq
            i += 1
        else:
            result[idx] = rt_sq
            j -= 1
    return result