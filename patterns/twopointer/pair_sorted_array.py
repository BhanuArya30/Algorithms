# Time O(n)
def pair_sorted_array(arr:list, target:int)->list:
    i = 0
    j = len(arr) - 1
    while i < j:
        tot = arr[i] + arr[j]
        if  tot == target:
            return [arr[i], arr[j]]
        elif tot > target:
            j -= 1
        else:
            i += 1
    return []


if __name__== "__main__":
    arr = [2,3,5,7,11,13]
    target = 14
    print(pair_sorted_array(arr, target))