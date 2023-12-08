def twoNumberSum(array, targetSum):
    pot = {}
    for idx, val in enumerate(array):
        if val in pot:
            return [val, targetSum]
        else:
            pot[targetSum - val] = idx
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))
