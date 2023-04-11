# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    sum_tree(root, 0, sums)
    
    return sums
    

def sum_tree(node, run_sum, sums):
    if not node:
        return 

    run_sum += node.value

    if not node.right and not node.left:
        sums.append(run_sum)
    
    sum_tree(node.left, run_sum, sums)
    sum_tree(node.right, run_sum, sums)
