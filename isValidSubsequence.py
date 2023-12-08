# Time O(n) | Space O(1)
# def isValidSubsequence(array, sequence):
#     i, j = 0, 0
#     while i < len(array) and j < len(sequence): # arr[1, 2, 3, 4], seq[2, 4] 
#         if array[i] == sequence[j]:
#             j += 1
#         i += 1
#     return len(sequence) == j

# Time O(n) | Space O(1)
# Optimized version - for loop for readability, break the loop if found substring earlier
def isValidaSubsequence(array, sequence):
    j = 0
    for num in array:
        if num == sequence[i]:
            j += 1
        if j == len(sequence):
            break
    return l == len(sequence)
