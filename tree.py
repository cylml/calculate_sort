class Node:
    def __init__(self, name, f_type="dir"):
        self.name = name
        self.type = f_type
        self.children = []
        self.parent = None

    def __repr__(self):
        return self.name


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        # name以 / 结尾
        if name[-1] != "/":
            name += "/"
        dir1 = Node(name)
        self.now.children.append(dir1)
        dir1.parent = self.now

    def ls(self):
        return self.now.children

    def cd(self, name):
        # 支持相对路径
        if name[-1] != "/":
            name += "/"
        elif name == "../":
            if self.now.parent:
                self.now = self.now.parent
                return
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return

        raise ValueError("invalid dir")


fs = FileSystemTree()
fs.mkdir("var")
fs.mkdir("root")
fs.mkdir("bin")
fs.cd("bin")
fs.cd("../")
# print(fs.root.children)
print(fs.ls())
