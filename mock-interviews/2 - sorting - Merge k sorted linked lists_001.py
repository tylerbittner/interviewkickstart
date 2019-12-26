"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its time and space complexity.
Assume that the total number of elements across all linked lists is N 

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_ll(values):
    head = None
    prev = None
    for val in values:
        node = Node(val)
        if prev:
            prev.next = node
        if not head:
            head = node
        prev = node
    return head

def print_ll(node):

    while node:
        print(f'{node.val}->', end='')
        node = node.next
    print()


def merge(lls: list) -> Node:

    # base case
    if len(lls) == 1:
        return lls[0]
    elif len(lls) < 1:
        return []

    # recursively do left & right
    mid = len(lls) // 2
    left = merge(lls[:mid])
    right = merge(lls[mid:])

    # combine
    head = None
    prev = None
    curr = None
    while left and right:
        if left.val <= right.val:
            curr = left
            left = left.next
        else:
            curr = right
            right = right.next

        curr.next = None
        if prev:
            prev.next = curr
        prev = curr
        if not head:
            head = curr

    leftovers = left or right
    if curr:
        curr.next = leftovers
    if not head:
        head = leftovers

    return head

#---
# TESTS
#---
lls = [
    create_ll([1,4,5]),
    create_ll([1,3,4]),
    create_ll([2,6])
]

for ll in lls:
    print_ll(ll)

result = merge(lls)
print_ll(result)

