import random
import sys

from cac_fuc.bst import BiTreeNode, BST


class AVLBNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0  # 平衡度


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)
        for var in li:
            self.insert_no_rec(var)

    def rotate_left(self, p, c):
        s2 = c.l_child
        p.r_child = s2
        if s2:
            s2.parent = p
        c.l_child = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.r_child
        p.l_child = s2
        if s2:
            s2.parent = p
        c.r_child = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        g = c.l_child

        s3 = g.r_child
        c.l_child = s3
        if s3:
            s3.parent = c
        g.r_child = c
        c.parent = g

        s2 = g.l_child
        p.l_child = s2
        if s2:
            s2.parent = p
        g.l_child = p
        p.parent = g

        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:  # s1,s2,s3,s4都为空，插入的实际上为g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.r_child
        s3 = g.r_child
        p.l_child = s3
        if s3:
            s3.parent = p
        g.r_child = p
        p.parent = g

        s2 = g.l_child
        c.r_child = s2
        if s2:
            s2.parent = c
        g.l_child = c
        c.parent = g

        if g.bf > 0:
            p.bf = 0
            c.bf = -1
        elif g.bf < 0:
            p.bf = 1
            c.bf = 0
        else:  # s1,s2,s3,s4都为空，插入的实际上为g
            p.bf = 0
            c.bf = 0
        g.bf = 0
        return g

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = AVLBNode(val)
            return
        while True:
            if val < p.data:
                if p.l_child:
                    p = p.l_child
                else:
                    p.l_child = AVLBNode(val)
                    p.l_child.parent = p
                    node = p.l_child  # node 存储的就是插入的节点
                    break
            elif val > p.data:
                if p.r_child:
                    p = p.r_child
                else:
                    p.r_child = AVLBNode(val)
                    p.r_child.parent = p
                    node = p.r_child
                    break
            else:
                return

        # 2.更新balance factor

        while node.parent:  # node.parent不空
            if node.parent.l_child == node:  # 传递是从左子树来的，左子树更沉了
                # 更新node.parent的bf -= 1
                if node.parent.bf < 0:  # 原来node.parent的bf == -1, 更新后变成-2
                    # 看node哪边沉
                    x = node.parent
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得 把n和g连接起来
                    # g.l_child = n
                elif node.parent.bf > 0:  # 原来node.parent的bf == 1, 更新后变成0
                    node.parent.bf = 0
                    return
                else:  # 原来node.parent的bf == 0, 更新后变成-1 继续传递
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:  # 传递是从右子树来的，右子树更沉了
                if node.parent.bf < 0:
                    node.parent.bf = 0
                    return
                elif node.parent.bf > 0:  # 原来node.parent的bf == 1, 更新后变成2
                    g = node.parent.parent  # 为了连接旋转之后的子树
                    x = node.parent
                    if node.bf > 0:
                        n = self.rotate_left(node.parent, node)
                    else:
                        n = self.rotate_right_left(node.parent, node)
                else:  # 原来node.parent的bf == 0, 更新后变成1 继续传递
                    node.parent.bf = 1
                    node = node.parent
                    continue
            # 3.连接旋转之后的子树

            n.parent = g
            if g:  # g不是空
                if x == g.l_child:  # 该node已经旋转了，不可继续使用
                    g.l_child = n
                else:
                    g.r_child = n
                break
            else:
                self.root = n
                break

sys.setrecursionlimit(20000)
li = [i for i in range(1, 100)]
random.shuffle(li)
print(li)
print()
# li = [45, 42, 41, 64, 63, 89, 5, 15, 7, 19, 60, 85, 82, 4, 69, 73, 93, 51, 34, 20, 18, 38, 50, 6, 9, 46, 59, 27, 32, 17, 57, 62, 47, 58, 23, 79, 24, 95, 44, 86, 83, 96, 88, 1, 35, 43, 65, 12, 16, 37, 81, 90, 54, 33, 31, 78, 91, 71, 21, 56, 98, 52, 76, 14, 10, 8, 3, 29, 67, 48, 99, 49, 70, 26, 66, 72, 92, 40, 22, 11, 25, 61, 68, 77, 75, 87, 39, 94, 13, 36, 55, 30, 84, 2, 53, 80, 28, 74, 97]
tree = AVLTree(li)
tree.in_order(tree.root)
