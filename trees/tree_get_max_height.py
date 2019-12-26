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

def get_max_height(root):
    if not root:
        return -1
    else:
        return 1 + max(get_max_height(root.left),  get_max_height(root.right))



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
#                 \
#                  20
#
node1_1 = Node(5, Node(3), Node(7))
node1_2 = Node(15, Node(13), Node(17, right=Node(20)))
root1 = Node(10, node1_1, node1_2)

assert get_max_height(root1) == 3
assert get_max_height(Node(10)) == 0
assert get_max_height(None) == -1
