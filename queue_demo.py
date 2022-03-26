# 队列先进先出
class Queue:
    def __init__(self, size=100):
        self.queue = [0 for i in range(size)]
        self.size = size
        self.rear = 0  # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element

    def pop(self):
        self.front = (self.front + 1) % self.size
        return self.queue[self.front]  # 不删只用返回下标

    def is_empty(self):
        return self.rear == self.front

    # 判断队满
    def is_filled(self):
        return (self.rear + 1) % self.size == self.front



