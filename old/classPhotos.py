#  Time O(n) | Space O(1)
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    
    counter = 0
    
    for r, c in zip(redShirtHeights, blueShirtHeights):
        if r > c:
            counter += 1
        elif r < c:
            counter -= 1
        else:
            return False
    
    return abs(counter) == len(redShirtHeights)
