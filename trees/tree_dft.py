#------------------------------------------------------------------------------
# >>> START SETUP CODE
#------------------------------------------------------------------------------
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)
#------------------------------------------------------------------------------
# <<< END SETUP CODE
#------------------------------------------------------------------------------


def dft(node, path=None):
    """
    steps:
    null checks (don't need to be done below!)
    init path
    append this node's val
    dft(node.left, path) recursively

    left/deepest branch is exhausted at this point
    call dft(node.right, path) rec.

    return path
    """

    if not node:
        return path
    if not path:
        path = []
    path.append(node.val)
    dft(node.left, path)
    dft(node.right, path)

    return path



#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------

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
root1 = Node(10, node1_1, node1_2)

assert dft(root1) == [10, 5, 3, 7, 15, 13, 17]