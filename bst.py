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


bst = BST([7, 6, 9, 1, 5, 2, 3])
bst.in_order(bst.root)
