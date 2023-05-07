# 1 - Minimum Waiting Time
def minimumWaitingTime(queries):
    queries.sort()
    query_wait = 0
    total_wait = 0

    for query in queries:
        total_wait += query_wait
        query_wait += query 

    return total_wait

def minimumWaitingTime2(queries):
    # multiply the remaining queries by delay time and sum them up 
    queries.sort()
    total = 0
    for i, query in enumerate(queries):
        left = len(queries) - (i+1)
        total += query * left
    
    return total

#print(minimumWaitingTime2([3, 2, 1, 2, 6]))

# Problem 2 - Clas Photos
# Complexity: time = O(n * log(n)), space = O(n)
def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[-1] > blueShirtHeights[-1]:
        backRow, frontRow = redShirtHeights, blueShirtHeights
    else:
        backRow, frontRow = blueShirtHeights, redShirtHeights

    for i in range(len(backRow)):
        if backRow[i] <= frontRow[i]:
            return False
    
    return True

# Complexity: time = O(n * log(n)), space = O(1)
def classPhotos2(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    diff = redShirtHeights[-1] - blueShirtHeights[-1]

    for i in range(len(redShirtHeights)):
        if (redShirtHeights[i] - blueShirtHeights[i]) * diff <= 0:
            return False
    
    return True

#print(classPhotos2([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))


# Problem 3 - Tandem Bicycle
# Time complexity: O(n*log(n)), Space: O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)

    result = 0
    for i in range(len(redShirtSpeeds)):
        result += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return result

def tandemBicycle_pythonic(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    
    return sum(max(redShirtSpeeds[i], blueShirtSpeeds[i]) for i in range(len(redShirtSpeeds)))

def tandemBicycle_reverse(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    if fastest:
        reverse_in_place(blueShirtSpeeds)

    result = 0
    for i in range(len(redShirtSpeeds)):
        result += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return result

def reverse_in_place(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

print(tandemBicycle_reverse([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))