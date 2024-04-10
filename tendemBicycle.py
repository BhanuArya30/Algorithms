# Time O(nlog(n)) | Space O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    result = 0
    
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds.sort(reverse=True)
    else:
        blueShirtSpeeds.sort()

    for red, blue in zip(redShirtSpeeds, blueShirtSpeeds):
        result += max(red, blue)

    return result

# The max of 2 elements in sorted arrays will be fastest when one array 
# is ascending and other is descending