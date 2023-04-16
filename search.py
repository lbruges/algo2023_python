def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    
    while left <= right:
        middle = round((left+right)/2)
        p_match = array[middle]
        if p_match == target:
            return middle
        elif p_match > target:
            right -=1
        else:            
            left += 1
            
    return -1


binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33)