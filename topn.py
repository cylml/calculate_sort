import random

from cac_fuc.sort import random_n


def sift(li, low, high):  # 有序时
    """
    :param li: 传入的列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low
    j = i * 2 + 1  # 开始位置的左孩子
    tmp = li[i]  # 把堆存起来
    while j <= high:
        if j + 1 <= high and li[j] > li[j + 1]:  # 右孩大于左孩(并且存在)
            j += 1  # 指向右孩
        # print(j)
        if li[j] < tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp更大
            break
    li[i] = tmp


def top_n(li, length):
    # 构造堆
    heap = li[0:length]
    for i in range(length // 2 - 1, -1, -1):
        # print(i)
        sift(heap, i, length - 1)
    minimum = heap[0]
    # print(len(li[length:]))
    for i in li[length:]:
        if i > minimum:
            heap[0] = i
            sift(heap, 0, length - 1)
            minimum = heap[0]
    # 出数，排好序
    for i in range(length - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    print(str(heap))


if __name__ == '__main__':
    # lib = []
    lib = random_n()
    top_n(lib, 1000)
