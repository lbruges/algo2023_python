# This is the class of the input root. Do not edit it.
# Problem 1 - Branch Sums
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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


# Problem 2 - Node Depths
def nodeDepths_recursive(root):
    # Write your code here.
    depth = calculate_depth(root, 0)
    return depth

def calculate_depth(node, depth):
    if not node:
        return 0
    return depth + calculate_depth(node.left, depth + 1) + calculate_depth(node.right, depth + 1)


def nodeDepths_stack(root):
    total_depth = 0
    nodes = [(root, 0)]

    while nodes:
        node, depth = nodes.pop() 
        if not node:
            continue
        total_depth += depth
        nodes.append((node.left, depth + 1))
        nodes.append((node.right, depth + 1))

    return total_depth

# Problem 3 - Evaluate Expression Tree
# Time: O(n), Space: O(h), h being the height
def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value

    left = evaluateExpressionTree(tree.left)
    right = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return left + right
    if tree.value == -2:
        return left - right
    if tree.value == -3:
        return int(left / right)
    if tree.value == -4:
        return left * right