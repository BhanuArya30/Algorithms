#  Time O(n) | Space
def reverse_array(arr:list[int])-> list[int]:
    begin = 0
    end = len(arr) - 1
    
    if len(arr) == 0:
        return None
    
    if len(arr) == 1:
        return arr

    while begin < end:
        arr[begin], arr[end] = arr[end], arr[begin]
        begin += 1
        end -= 1
    return  arr

if __name__ == "__main__":
    print(reverse_array([1,2,3,4]))
    print(reverse_array([1,2,3,4,5]))