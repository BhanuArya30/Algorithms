def find_median_sorted_arrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    total_len = m + n
    median_index2 = total_len // 2
    
    i, j = 0, 0
    current, previous = 0, 0
    count = 0
    
    while count <= median_index2:
        previous = current
        if i < m and (j >= n or nums1[i] < nums2[j]):
            current = nums1[i]
            i += 1
        else:
            current = nums2[j]
            j += 1
        count += 1
    
    if total_len % 2 == 1:
        return current
    else:
        return (current + previous) / 2

nums1 = [1, 3]
nums2 = [2, 4]
print(find_median_sorted_arrays(nums1, nums2))