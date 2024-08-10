"""Merge with Duplicates Removal

Problem:
You are given two sorted integer arrays nums1 and nums2. Merge the two arrays into one sorted array, but remove any duplicate elements from the final array.

Example:

    Input: nums1 = [1, 2, 2, 3], nums2 = [2, 3, 4, 5]
    Output: [1, 2, 3, 4, 5]"""


def merge_without_duplicates(arr1, arr2):
    i = 0
    j = 0   
    seen = set()
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if arr1[i] not in seen:
                seen.add(arr1[i])
                result.append(arr1[i])
            i += 1
        else:
            if arr2[j] not in seen:
                seen.add(arr2[j])
                result.append(arr2[j])
            j += 1

    while i < len(arr1):
        if arr1[i] not in seen:
            seen.add(arr1[i])
            result.append(arr1[i])
        i += 1

    while j < len(arr2):
        if arr2[j] not in seen:
            seen.add(arr2[j])
            result.append(arr2[j])
        j += 1
    print(result)
    return result


def find_k_smallest(arr, k):
    if k > len(arr):
        return None
    return arr[k - 1]


nums1 = [1, 2, 2, 3, 5]
nums2 = [2, 3, 4, 4, 5]
# [1, 2, 3, 4, 5]


result = merge_without_duplicates(nums1, nums2)

print(find_k_smallest(result, 3))