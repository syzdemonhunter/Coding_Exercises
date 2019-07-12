# T: O(n)
# S: O(d)

def validateBst(tree):
    return helper(tree, -float('inf'), float('inf'))

def helper(tree, min_val, max_val):
    if not tree:
        return True
    if tree.value < min_val or tree.value >= max_val:
        return False
    left_valid = helper(tree.left, min_val, tree.value)
    right_valid = helper(tree.right, tree.value, max_val)
    return left_valid and right_valid


#######################
 def validateBst(tree):
    if not tree:
        return True
    return helper(tree, None, None)

def helper(root, lower, upper):
    if not root:
        return True
    if lower and root.value < lower.value:
        return False
    if upper and root.value >= upper.value:
        return False
    return helper(root.left, lower, root) \
       and helper(root.right, root, upper) 