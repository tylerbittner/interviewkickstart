from collections import deque
# For debugging
import time


#-----
# Define Node class
#-----
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)

#-----
# DFT - recursive
#-----
def dft(root, path=None):
    '''Depth-first traversal (recursively). Returns list w/ values in path.'''
    if not root:
        return path
    if not path:
        path = []

    print(root.val, end=' ')
    path.append(root.val)
    dft(root.left, path)
    dft(root.right, path)
    return path


#-----
# DFT - iterative
#-----
def dft_iter(root):
    '''Depth-first traversal (iteratively). Returns list w/ values in path.'''
    if root is None:
        return
    stack = [root]
    path = []
    while stack:
        node = stack.pop()
        path.append(node.val)
        print(node.val, end=' ')
        # Note we must add to the stack in *reverse* order to be processed (right then left)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return path

#-----
# BFT - iterative
#-----
def bft(root):
    '''Breadth-first traversal, or "level-order", of tree'''
    if root is None:
        return path
    queue = deque([root])
    path = []
    while queue:
        node = queue.popleft()
        path.append(node.val)
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return path


#-----
# BST insert
#-----
def insert_bst(root, val):
    '''Insert new node into BST, returning root node of updated tree'''
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root


#-----
# BST lookup
#-----
def lookup_bst(root, val):
    '''Return first node found with given value'''
    
    if root is None:
        print(f'NO value {val} found in tree')
        return None
    if root.val == val:
        print(f'Found value {val} in tree; returning node')
        return root
    if val < root.val:
        return lookup_bst(root.left, val)
    else:
        return lookup_bst(root.right, val)


#-----
# BST delete
#-----
def delete_bst(root, val, parent=None):
    '''Delete first node found with given value; return root of updated tree.'''
    
    # Case: empty tree or val not found
    if root is None:
        print(f'DEBUG: value {val} not found in tree')
        return

    if root.val == val:
        # Case: leaf
        if root.left is None and root.right is None:
            # TODO: delete the parent's correct child reference
            # TODO: DEBUG this -- fails when parent is null
            if parent.val < val:
                parent.right = None
            else:
                parent.left = None

        # Case: 1 child
        elif root.left is not None:
            root.val = root.left.val
            root.left = None
        elif root.right is not None:
            root.val = root.right.val
            root.right = None
        
        # Case: 2 children
        else:
            #replacement_node = find_successor_bst(root.right, val)
            delete_bst(root.right, replacement_node.val)
            root.val = replacement_node.val

    elif val < root.val:
        delete_bst(root.left, val, root)
    else:
        delete_bst(root.right, val, root)

    return root

#-----
# Create test tree(s)
#-----

# EXAMPLE TREE 1
#
#       10
#     _/  \_ 
#    /      \ 
#   5        15
#  / \      /  \
# 3   7    13   17
#
node1_1 = Node(5, Node(3), Node(7))
node1_2 = Node(15, Node(13), Node(17))
tree1 = Node(10, node1_1, node1_2)

# EXAMPLE TREE X
#
#       5
#     _/ \_ 
#    /     \ 
#   5       5
#  / \       \
# 5   5       5
#


#---
# Run & assert correctness of DFT & BFT
# TODO: Add assertions and more test cases
#---
print('Calling dft()...')
assert dft(tree1) == [10, 5, 3, 7, 15, 13, 17]
print('\n')

print('Calling dft_iter()...')
assert dft_iter(tree1) == [10, 5, 3, 7, 15, 13, 17]
print('\n')

print('Calling bft()...')
assert bft(tree1) == [10, 5, 15, 3, 7, 13, 17]
print('\n')

print('Calling insert_bst(tree1, 6)...')
result = insert_bst(tree1, 6)
assert dft(result) == [10, 5, 3, 7, 6, 15, 13, 17]
print('\n')

print('Calling insert_bst(tree1, 20)...')
result = insert_bst(tree1, 20)
assert dft(result) == [10, 5, 3, 7, 6, 15, 13, 17, 20]
print('\n')

print('Calling insert_bst(None, 100)... [case: empty tree passed]')
result = insert_bst(None, 100)
assert dft(result) == [100]
print('\n')

print('Calling lookup_bst(tree1, 13)...')
result_node = lookup_bst(tree1, 13)
assert result_node.val == 13

print('Calling lookup_bst(tree1, 1000)... [case: not found]')
result_node = lookup_bst(tree1, 1000)
assert result_node == None
print('\n')

print('Calling delete_bst(tree1, 13)... [delete leaf (parent\'s left)]')
result_root = delete_bst(tree1, 13)
assert dft(result_root) == [10, 5, 3, 7, 6, 15, 17, 20]
print('\n')

print('Calling delete_bst(tree1, 20)... [delete leaf (parent\'s right)]')
result_root = delete_bst(tree1, 20)
assert dft(result_root) == [10, 5, 3, 7, 6, 15, 17]
print('\n')

print('Calling delete_bst(tree1, 17)... [delete node w/ one child]')
result_root = delete_bst(tree1, 17)
assert dft(result_root) == [10, 5, 3, 7, 6, 15]
print('\n')

print('Calling delete_bst(tree1, 5)... [delete node w/ two children]')
result_root = delete_bst(tree1, 5)
assert dft(result_root) == [10, 3, 7, 6, 15]
print('\n')

print('Calling delete_bst(Node(42), 42)... [delete only node]')
assert delete_bst(Node(42), 42) == None
print('\n')

print('Calling delete_bst(tree1, 42)... [node not found]')
assert delete_bst(tree1, 42) == None
print('\n')
