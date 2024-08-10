# def merge_sorted_arrays(arr1, arr2):
#     merged_array = []
#     i=0
#     j=0

#     for _ in range(len(arr1) + len(arr2)):
#         if i<len(arr1) and (j>=len(arr2) or arr1[i] <= arr2[j]):
#             merged_array.append(arr1[i])
#             i += 1
#         else:
#             merged_array.append(arr2[j])
#             j+= 1

#     return merged_array

# j >= len(arr2): Checks if all elements from arr2 have been processed. 
# If j (index for arr2) has reached or exceeded the length of arr2, it means arr2 is exhausted. 
# In this case, we should take elements from arr1 because arr2 has no more elements to contribute.

def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
        
    # remaining
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    
    return result

# # time O(nlogn)
# def merge_sorted_arrays(arr1, arr2):
#     return sorted(arr1 + arr2)

# Example usage:
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
result = merge_sorted_arrays(arr1, arr2)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]