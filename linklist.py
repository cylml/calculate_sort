class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def create_linklist(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node

    return head


def create_linklist_tail(li):
    tail = Node(li[0])
    head = tail
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node

    return head


def query(lk, ind):
    while ind > 0:
        # print(lk.item, end=",")
        ind -= 1
        try:
            lkn = lk.next
            if lkn:
                print(lk.item)
                lk = lkn
        except AttributeError:
            raise IndexError("超过链表长度")
    return lk


# 插入在ind位后面
def insert(lk, ind, val):
    ind = ind - 1
    current_node = query(lk, ind)
    if ind > 0:
        if current_node:
            # print(bool(current_node))
            next_node = current_node.next
            ins_node = Node(val)
            current_node.next = ins_node
            ins_node.next = next_node
        else:
            current_node.next = Node(val)
    elif ind == -1:
        v1 = lk.item
        lk.item = val
        node = Node(v1)
        node.next = lk.next
        lk.next = node
    else:
        current_node.next = Node(val)
    return lk


def pop(lk, ind):
    if ind > 0:
        ind = ind - 1
        current_node = query(lk, ind)
        p = current_node.next
        current_node.next = current_node.next.next
        del p
    else:
        lk = lk.next
    return lk


def print_linklist(lk):
    while lk:
        print(lk.item, end=",")
        lk = lk.next


lk = create_linklist_tail([1, 2, 3])
insert(lk, 4, 5)
print_linklist(lk)
print()
pop(lk, 1)
print_linklist(lk)
# print(query(lk, 1).item)
