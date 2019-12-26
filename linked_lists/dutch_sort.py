'''
Problem statement: 
Given a linked list and value x, sort the list into 3 partitions: < x, == x, and > x.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def dutch_sort(node, x: int) -> None:

    h1, p1, h2, p2, h3, p3 = [None] * 6
    while node:
        # print(f'current node.val={node.val}, next={node.next}')
        if node.val < x:
            p1 = append(p1, node)
            p1.next = None
            if not h1:
                h1 = node
        elif node.val == x:
            if not h2:
                h2 = node
            p2 = append(p2, node)
        else:
            if not h3:
                h3 = node
            p3 = append(p3, node)
        node = node.next

    # append the 3 parts
    # 3-->2 or 3-->1, 2-->1
    print(f'\th1:')
    print_ll(h1)
    print(f'\th2:')
    print_ll(h2)
    print(f'\th3:')
    print_ll(h3)
    append(p1, h2)
    append(p2, h3)

    # if h3:
    #     if p2:
    #         p2.next = h3
    #     elif p1:
    #         p1.next = h3
    # if h2 and p1: 
    #     p1.next = h2


def append(n1, n2):
    '''Append node 1 to node 2'''
    next_node = n1
    if n1:
        print(f'appending {n1.val} and {n2.val}')
        n1.next = n2
    if n2:
        next_node = n2
    print(f'Returning next_node.val={next_node.val}')
    return next_node


#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------
def print_ll(node):
    while node:
        print(f'{node.val}->', end='')
        node = node.next
    print()


def create_ll(values) -> Node:
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


# 3 partitions present
ll = create_ll([14, 2, 8, 3, 5, 6, 45, 6, 12])
print(f'Input:')
print_ll(ll)
dutch_sort(ll, 6)
print('Expect: \n2->3->5->6->6->14->8->45->12->')
print('Result:')
print_ll(ll)

exit() 

# Only partition 1
ll = create_ll([6, 2, 8])
result = dutch_sort(ll, 10)
print('Expect: \n6->2->8->')
print('Result:')
print_ll(result)

# Only partition 2
ll = create_ll([6, 6, 6])
result = dutch_sort(ll, 6)
print('Expect: \n6->6->6->')
print('Result:')
print_ll(result)

# Only partition 3
ll = create_ll([6, 2, 8])
result = dutch_sort(ll, 1)
print('Expect: \n6->2->8->')
print('Result:')
print_ll(result)

# Only partition 1 and 3
ll = create_ll([6, 2, 8])
result = dutch_sort(ll, 5)
print('Expect: \n2->6->8->')
print('Result:')
print_ll(result)


# Only partition 2 and 3
ll = create_ll([6, 2, 8])
result = dutch_sort(ll, 2)
print('Expect: \n2->6->8->')
print('Result:')
print_ll(result)

