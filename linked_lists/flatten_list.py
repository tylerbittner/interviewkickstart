from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.child = None


def flatten_ll_w_queue(head) -> Node:
    q = deque()
    if head:
        q.append(head)
    tail = None
    while q:
        node = q.popleft()
        if tail:
            tail.next = node
        while node:
            # print(f'Processing node: {node.val}')
            tail = node
            if node.child:
                q.append(node.child)
                node.child = None
            node = node.next

    return head


def flatten_ll_no_aux_space(head) -> Node:
    node = tail = head
    while node:
        # print(f'Processing node using no_aux_space: val={node.val}, child={node.child}')
        if node.child:
            tail = get_tail(tail)
            tail.next = node.child
            node.child = None
        node = node.next
    return head


def get_tail(node) -> Node:
    tail = node
    while node:
        tail = node
        node = node.next
    # print(f'\tReturning tail: {tail.val}')
    return tail


#------------------------------------------------------------------------------
# TESTS
#------------------------------------------------------------------------------
def print_ll(node):
    while node:
        print(f'{node.val}->', end='')
        if node.child:
            print(f'[has children] ', end='')
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


def test_create_ll_w_children_1() -> Node:
    values = {14: [],
        8: [9, 10],
        3: [4],
        5: []
        }
    head = None
    prev = None
    print(f'values={values}')
    for val, children in values.items():
        # print(f'val, children={val}, {children}')
        node = Node(val)
        if children:
            child_head = create_ll(children)
            node.child = child_head
        if prev:
            prev.next = node
        if not head:
            head = node
        prev = node
    return head


mult_ll = test_create_ll_w_children_1()
result = flatten_ll_w_queue(mult_ll)
print('Expected from flatten_ll_w_queue():\n14->8->3->5->9->10->4->')
print('Result:')
print_ll(result)

mult_ll = test_create_ll_w_children_1()
result = flatten_ll_no_aux_space(mult_ll)
print('Expected from flatten_ll_no_aux_space():\n14->8->3->5->9->10->4->')
print('Result:')
print_ll(result)
