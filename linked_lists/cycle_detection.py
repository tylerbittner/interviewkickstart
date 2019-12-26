class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_cycle(node) -> bool:
    slow = node
    fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # Cycle found
            return True
    # No cycle found
    return False


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



#---
# TEST CODE
#--- 

def test_create_cycle_1() -> Node:

    # Create linked list
    head = create_ll([1, 4, 5, 9, 11, 14])
    print(f'created node: {head}')
    print_ll(head)
    cycle_start_val = 5
    cycle_start_node = None
    
    # Create cycle in it
    node = head
    prev = None
    while node:
        if node.val == cycle_start_val:
            cycle_start_node = node
        prev = node
        node = node.next
        
    # link last node to cycle start
    prev.next = cycle_start_node

    return head


ll_no_cycle = create_ll([1, 4, 5, 9, 11, 14])
print(f'll_no_cycle:')
print_ll(ll_no_cycle)

ll_cycle_1 = test_create_cycle_1()
# This will loop infinitely
# print(f'll_cycle_1:')
# print_ll(ll_cycle_1)

for ll in [ll_no_cycle, ll_cycle_1]:
    if detect_cycle(ll):
        print('Cycle found!')
    else:
        print('NO cycle found.')



