class MinMaxStack_NotOptimal:

    def __init__(self):
        self.stack = []
        self.min_max = []
    
    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not self.stack:
            return None
        
        to_pop = self.stack[-1]
        
        pos = None
        for i, el in enumerate(self.min_max):
            if el == to_pop:
                pos = i
                break
        
        self.min_max.pop(pos)
        
        
        print("popping", self.min_max)
        
        return self.stack.pop()

    def push(self, number):
        self.stack.append(number)
        self.insertMinMax(number)


    def getMin(self):
        if not self.min_max:
            return None
        
        return self.min_max[0]

    def getMax(self):
        if not self.min_max:
            return None
            
        return self.min_max[-1]

    def insertMinMax(self, num):
        pos = 0
        isMax = True
        
        for i in range(len(self.min_max)):
            pos = i
            if self.min_max[i] >= num:
                isMax = False
                break
        if isMax:
            self.min_max.append(num)
        else:
            self.min_max.insert(pos, num)
        
        print("insert", self.min_max)

# Feel free to add new properties and methods to the class.
class MinMaxStack_ThreeArr:

    def __init__(self):
        self.stack = []
        self.min = []
        self.max = []
    
    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not self.stack:
            return None
        
        to_pop = self.peek()
        
        if to_pop == self.min[-1]:
            self.min.pop()

        if to_pop == self.max[-1]:
            self.max.pop()
        
        return self.stack.pop()

    def push(self, number):
        if not self.stack:
            self.min.append(number)
            self.max.append(number)
        else:
            if number <= self.min[-1]:
                self.min.append(number)
            if number >= self.max[-1]:
                self.max.append(number)
        
        self.stack.append(number)

    
    def getMin(self):
        if not self.min:
            return None
        
        return self.min[-1]

    def getMax(self):
        if not self.max:
            return None
            
        return self.max[-1]
    
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_max = []
    
    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def pop(self):
        if not self.stack:
            return None
        
        self.min_max.pop()
        return self.stack.pop()

    def push(self, number):
        if not self.stack:
            self.min_max.append((number, number))
        else:
            curr_min, curr_max = self.min_max[-1]
            new_min = min(curr_min, number)
            new_max = max(curr_max, number)
            self.min_max.append((new_min, new_max))
               
        self.stack.append(number)

    
    def getMin(self):
        if not self.min_max:
            return None
        
        return self.min_max[-1][0]

    def getMax(self):
        if not self.min_max:
            return None
            
        return self.min_max[-1][1]


stack = MinMaxStack()
stack.push(2)
print(stack.getMin())
print(stack.getMax())
print(stack.peek())
stack.push(7)
print(stack.getMin())
print(stack.getMax())
print(stack.peek())
stack.push(1)
print(stack.getMin())
print(stack.getMax())
print(stack.peek())
stack.push(8)
print(stack.getMin())
print(stack.getMax())
print(stack.peek())
stack.push(3)
print(stack.getMin())
print(stack.getMax())
print(stack.peek())
stack.push(9)
print(stack.getMin())
print(stack.getMax())
print(stack.peek())
print(stack.pop())
print(stack.getMin())
print(stack.getMax())
print(stack.peek())
print(stack.pop())
print(stack.getMin())
print(stack.getMax())
print(stack.peek())

print(stack.pop())
print(stack.getMin())
print(stack.getMax())
print(stack.peek())
print(stack.pop())
print(stack.getMin())
print(stack.getMax())
print(stack.peek())

print(stack.pop())
