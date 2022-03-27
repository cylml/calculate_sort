from collections import deque


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.l_child = None
        self.r_child = None
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def level_order(self, root):
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            node = queue.popleft()
            print(node.data, end=",")
            if node.l_child:
                queue.append(node.l_child)
            if node.r_child:
                queue.append(node.r_child)

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.l_child = self.insert(node.l_child, val)
            node.l_child.parent = node
        elif val > node.data:
            node.r_child = self.insert(node.r_child, val)
            node.r_child.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if not p.l_child:
                    p.l_child = BiTreeNode(val)
                    p.l_child.parent = p
                    return
                p = p.l_child
            elif val > p.data:
                if not p.r_child:
                    p.r_child = BiTreeNode(val)
                    p.r_child.parent = p
                    return
                p = p.r_child
            else:
                return

    # 前序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            self.pre_order(root.l_child)
            self.pre_order(root.r_child)

    # 中序排序
    def in_order(self, root):
        if root:
            self.in_order(root.l_child)
            print(root.data, end=",")
            self.in_order(root.r_child)

    # 后序排序
    def post_order(self, root):
        if root:
            self.post_order(root.l_child)
            self.post_order(root.r_child)
            print(root.data, end=",")

    def query(self, node: BiTreeNode, val):
        if not node:
            return None
        if node.data > val:
            return self.query(node.l_child, val)
        elif node.data < val:
            return self.query(node.r_child, val)
        else:
            print(node.data)
            return node

    def query_no_rec(self, val) -> BiTreeNode:
        p = self.root
        if p.data == val:
            return p
        while p:
            if p.data > val:
                if not p.l_child:
                    return
                if p.l_child.data == val:
                    return p.l_child
                p = p.l_child
            elif p.data < val:
                if not p.r_child:
                    return
                if p.r_child.data == val:
                    return p.r_child
                p = p.r_child

    # def query_no_rec1(self, val):
    #     p = self.root
    #     while p:
    #         if p.data > val:
    #             return p.l_child
    #         elif p.data < val:
    #             return p.r_child
    #         else:
    #             return p
    #     return None

    # FIXME 删不掉头节点
    def pop(self, val):
        node = self.query_no_rec(val)
        if node:
            # flag = False
            parent = node.parent
            # if not parent:
            #     self.root = None
            # 节点为最后一个
            if node.l_child is None and node.r_child is None:
                if parent.data > node.data:
                    parent.l_child = None
                    # node.parent = None
                    del node
                else:
                    parent.r_child = None
                    node.parent = None
                    del node
            elif node.l_child and node.r_child:
                r_c = node.r_child
                while r_c.l_child:
                    r_c = r_c.l_child
                if r_c.r_child:
                    c_p = r_c.parent
                    c_p.l_child = r_c.r_child
                    r_c.r_child = node.r_child
                # r_c.parent = parent
                if parent.data > node.data:
                    parent.l_child = r_c
                else:
                    parent.r_child = r_c
                r_c.l_child = node.l_child
                del node
            else:
                if node.l_child:
                    c_node = node.l_child
                else:
                    c_node = node.r_child
                if parent.data > node.data:
                    node.parent.l_child = c_node
                else:
                    node.parent.r_child = c_node
                del node


bst = BST([17, 5, 35, 2, 11, 9, 16, 7, 8, 29, 38])
bst.pop(17)
print()
bst.level_order(bst.root)
print()
# print(bst.query(bst.root, 2).data)
# print(bst.query_no_rec(17).data)
