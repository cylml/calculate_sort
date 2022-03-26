from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")
h = BiTreeNode("H")

e.l_child = a
a.r_child = c
c.l_child = b
c.r_child = d
e.r_child = g
g.r_child = f
"""
   E
   /\
  A  G
   \   \
    C   F
   / \
  B   D
"""

root = e
print(root.l_child.r_child.data)


# 前序遍历
def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.l_child)
        pre_order(root.r_child)


# 中序排序
def in_order(root):
    if root:
        in_order(root.l_child)
        print(root.data, end=",")
        in_order(root.r_child)


# 后序排序
def post_order(root):
    if root:
        post_order(root.l_child)
        post_order(root.r_child)
        print(root.data, end=",")


# 层次排序
def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=",")
        if node.l_child:
            queue.append(node.l_child)
        if node.r_child:
            queue.append(node.r_child)


pre_order(root)
print()
in_order(root)
print()
post_order(root)
print()
level_order(root)
