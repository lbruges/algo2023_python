# Problem 1 - Palindrome Check - O(n) time, O(1) space
"""
Note: if this gets resolved by creating a new reversed string and comparing it to the initial one, time complexity would be O(n**2)
Each time a String is modified, it'd iterate through all the characters to append newer ones
String == immutable
Using a list and concatenating at the end would improbe time complexity
"""
def isPalindrome(string):
    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -=1
    return True

#print(isPalindrome("abcdcba"))

# Problem 2 - Caesar Encryptor - time and space: O(n)
def caesarCipherEncryptor(string, key):
    # a: 97
    # z: 122
    if key == 0:
        return string
        
    result = []

    for c in string:
        c_shift = char_shift(c, key)
        result.append(c_shift)

    return "".join(result)

def caesarCipherEncryptor_oneLiner(string, key):
    return "".join(chr((((ord(c) - 97) + key) % 26) + 97) for c in string)


def char_shift(c, key):
    if ord(c) + key <= 122:
        return chr(ord(c) + key)
    else:
        num_c = ord(c) - 97
        new_c = (num_c + key) % 26
        return chr(new_c + 97)
    
#print(caesarCipherEncryptor_oneLiner("xyz", 2))

# Problem 3 -  Common Characters
def commonCharacters(strings):
    first = strings[0]
    res = { c: {0} for c in first }
    results = [] 

    for i in range(1, len(strings)):
        for c in strings[i]:
            if c in res:
                res[c].add(i)

    for key, val in res.items():
        if len(val) == len(strings):
            results.append(key)
    
    
    return results

def commonCharacters2(strings):
    small_set = set(get_smallest(strings))

    for st in strings:
        curr = set(st)
        for c in list(small_set):
            if c not in curr:
                small_set.remove(c)
    
    return small_set

def get_smallest(strings):
    smallest = strings[0]
    for i in range(0, len(strings)):
        if len(strings[i]) < len(smallest):
            smallest = strings[i]
    
    return smallest


print(commonCharacters2(["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"]))