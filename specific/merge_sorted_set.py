# Time O((n+m)log(n+m))
# def merge_sorted_sets(s1, s2):
#     union_set = s1.union(s2)
#     return sorted(union_set)


# Time O(n)
def merge_sorted_sets(s1, s2):
    list1 = sorted(s1)
    list2 = sorted(s2)
    i = 0
    j = 0
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    result.extend(list1[i:])
    result.extend(list2[j:])

    return result


# # Example 1
# set1 = {1, 3, 5, 7}
# set2 = {2, 3, 6, 8}

set1 = {10, 20, 30}
set2 = {5, 15, 25, 35}

# set1 = {}
# set2 = {}

print(merge_sorted_sets(set1, set2))
