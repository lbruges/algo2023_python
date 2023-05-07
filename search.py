# Problem 1 - Binary Search
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

# print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))

# Problem 2 - Three Largest Numbers
import sys

def findThreeLargestNumbers(array):
    largest = [-sys.maxsize, -sys.maxsize, -sys.maxsize]

    for num in array:
        check_insert(num, largest)

    return largest

def check_insert(num, arr):
    for i in range(2):
        if num >= arr[i]:
            if arr[i+1] < num:
                temp = arr[i+1]
                arr[i+1] = num
                arr[i] = temp
            else:
                arr[i] = num

print(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]))