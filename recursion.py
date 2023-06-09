# Problem 1 - Fibonacci Series
def getNthFib_iter(n):
    # Iterative -  Time: O(n), Space: O(n)
    fib = [0, 1]

    if n <= 2:
        return fib[n-1]
    
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    return fib[-1]

def getNthFib_rec(n):
    # Recursive -  Time: 2**n (each fib would result in 2 fib calls, and results are being re-calculated n number of times), Space: O(n)
    if n == 2:
        return 1
    if n == 1:
        return 0

    return getNthFib_rec(n-1) + getNthFib_rec(n-2)

def getNthFib_mem(n, mem={1:0, 2:1}):
    # Recursive + mem -  Time: O(n), Space: O(n)
    if n in mem:
        return mem[n]

    mem[n] = getNthFib_mem(n-1) + getNthFib_mem(n-2)
    return mem[n]

def getNthFib_alt(n):
    # Iterative -  Time: O(n), Space: O(1)
    a, b = 0, 1

    for _ in range(n-1):
        temp = a
        a = b
        b += temp
    
    return a

def getNthFib_alt2(n):
    # Iterative -  Time: O(n), Space: O(1)
    a, b = 0, 1

    for _ in range(n-1):
        a, b = b, a+b
    
    return a


#print(getNthFib_alt2(6))

# Problem 2 - Product Sum
# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    return sumAll_pythonic(array)

def sumAll(arr, depth=1, sum=0):
    for el in arr:
        if type(el) is list:
            sum += sumAll(el, depth+1)
        else:
            sum += el
    return depth * sum

def sumAll_pythonic(arr, depth=1):
    return depth * sum(sumAll_pythonic(el, depth+1) if isinstance(el, list) else el for el in arr)

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))