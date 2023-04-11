def findClosestValueInBst(tree, target):
    diff_target = abs(target - tree.value)
    closest = tree.value
    
    node = tree
    
    while node:
        val  = node.value
        diff = abs(target - val)
        if diff == 0:
            return val

        if val > target:
            node = node.left
        else:
            node = node.right
        
        if diff <= diff_target:
            diff_target = diff
            closest = val

    return closest
            


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
