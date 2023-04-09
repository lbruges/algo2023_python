def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1 
    while left != right:
        sum = array[left] + array[right]
        if targetSum == sum:
            return [array[left], array[right]]
        elif targetSum < sum:
            right -= 1
        else:
            left += 1

    return []

def isValidSubsequence(array, sequence):
    sub_index = 0
    
    for element in array:
        if sub_index == len(sequence):
            return True
        
        curr = sequence[sub_index]
        if element == curr:
            sub_index += 1
        
    return sub_index == len(sequence)


def isValidSubsequence2(array, sequence):
    arr_i = 0
    seq_i = 0
    
    while arr_i < len(array) and seq_i < len(sequence):
        if array[arr_i] == sequence[seq_i]:
            seq_i +=1
        arr_i += 1
    
    return seq_i == len(sequence)


def sortedSquaredArray(array):
    # Time: n * log(n)
    squares = sorted(map(lambda x: x**2, array))
    return squares

def sortedSquaredArray2(array):
    # ascending order - linear time O(n)
    res = [0 for _ in array]
    start = 0
    end = len(array) - 1

    for i in reversed(range(len(array))):
        if abs(array[start]) > abs(array[end]):
            res[i] = array[start] ** 2
            start += 1
        else:
            res[i] = array[end] ** 2
            end -= 1
    
    return res

print(sortedSquaredArray2([1, 2, 3, 5, 6, 8, 9]))
#print(isValidSubsequence2([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
#print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))