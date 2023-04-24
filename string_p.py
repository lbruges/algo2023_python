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


#print(commonCharacters2(["ab&cdef!", "f!ed&cba", "a&bce!d", "ae&fb!cd", "efa&!dbc", "eff!&fff&fffffffbcda", "eeee!efff&fffbbbbbaaaaaccccdddd", "*******!***&****abdcef************", "*******!***&****a***********f*", "*******!***&****b***********c*"]))

# Problem 4 - Run Length Encoding

def runLengthEncoding(string):
    c = string[0]
    res = []
    local_c = 0
    
    for i in range(len(string)):
        curr = string[i]
        if curr=="=":
            print("lel")
        if c == curr:
            local_c += 1
            if local_c == 9:
                res.append(f'9{c}')
                local_c = 0
        else:
            if local_c > 0:
                res.append(f'{local_c}{c}')
            c = curr
            local_c = 1

    res.append(f'{local_c}{c}')

    return "".join(res)

def runLengthEncoding_refactor(string):
    prev = None
    res = []
    local_c = 0
    
    for curr in string:
        if prev and (prev != curr or local_c == 9):
            res.append(f'{local_c}{prev}')
            local_c = 0
            
        prev = curr
        local_c += 1

    res.append(f'{local_c}{prev}')
    return "".join(res)

#print(runLengthEncoding_refactor("........______=========AAAA   AAABBBB   BBB"))

# Problem 5 - First Non-repeating Character
# O(n) time, O(1) space - no more than 27 letters - constant
def firstNonRepeatingCharacter(string):
    mem = dict()
    for char in string:
        if char in mem:
            mem[char] += 1
        else:
            mem[char] = 1

    for i in range(len(string)):
        char = string[i]
        if mem[char] == 1:
            return i
    
    return -1

# Get method - supports default value
def firstNonRepeatingCharacter2(string):
    mem = dict()
    
    for char in string:
        mem[char] = mem.get(char, 0) + 1
        
    for i in range(len(string)):
        char = string[i]
        if mem[char] == 1:
            return i
    
    return -1

#print(firstNonRepeatingCharacter2("abcdcaf"))

# Problem 6 - Semordnilap
# Time: O(n*m) , Space: O(n*m) where n is the number of words and m is the length of the longest word.
def semordnilap(words):
    w_set = set(words)
    res = []

    for word in words:
        reversed_s = reverse_str(word)
        if reversed_s != word and reversed_s in w_set:
            res.append([word, reversed_s])
            w_set.remove(word)
            w_set.remove(reversed_s)
    
    return res

def reverse_str(string):
    chars = []

    for i in reversed(range(len(string))):
        chars.append(string[i])

    return "".join(chars) 

# Using list slicing to revert string
def semordnilap2(words):
    w_set = set(words)
    res = []

    for word in words:
        reversed_s = word[::-1]
        if reversed_s != word and reversed_s in w_set:
            res.append([word, reversed_s])
            w_set.remove(word)
            w_set.remove(reversed_s)
    
    return res

#print(semordnilap2(["dog", "hello", "god", "olleh", "non"]))