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

# Time: optimal: Nlog(k)
# Space: N+k; optimal: O(1)
# NOTE: mergesort can be done WITHOUT aux space when using *linked lists*!  Practice implementing.


# i, j

"""
Iter 1:
1->4->5  1->3->4
1->1->3->4->4->5


Iter 2:
1->1->3->4->4->5 2->6
1->1->2->3->4->4->5->6


Prove time complexity:
Ex: k=12, k=6, k=3
"""

# STOPPED HERE DURING ACTUAL MOCK INTERVIEW

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'


def create_ll(data_values):
    '''Helper to create linked Nodes via an array of values.'''
    
    head = None
    prev_node = None
    for val in data_values:
        node = Node(val)
        if not head:
            head = node
        if prev_node:
            prev_node.next = node
        prev_node = node
    return head


def traverse(node):
    '''Helper to traverse & print linked list.'''
    output = ''
    while node:
        output = ''.join([output, str(node.data)])
        if node.next:
            output = ''.join([output, '->'])
        node = node.next
    return output


def merge(lists):

    if len(lists) == 1:
        # print(f'returning linked list: {traverse(lists[0])}')
        return lists[0]
    if len(lists) < 1:
        return None

    mid = len(lists) // 2
    left = merge(lists[:mid])
    right = merge(lists[mid:])

    head = None
    curr = None
    prev = None
    while left and right:
        if left.data <= right.data:
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

        # print(f'\tresult so far: {traverse(head)}')

    leftovers = left or right
    if curr:
        curr.next = leftovers
    else:
        head = leftovers

    # print(f'returning linked list: {traverse(head)}')
    return head



#---
#--- TESTS
#---

lists = [
    create_ll([1, 4, 5]),
    create_ll([1, 3, 4]),
    create_ll([2, 6])
]
print(f'input: ')
for l in lists:
    print(f'\t{traverse(l)}')
result = merge(lists)
print(f'Result: {traverse(result)}')



