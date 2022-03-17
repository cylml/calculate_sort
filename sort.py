import random
import sys
import time
from functools import wraps


def cal_time(fuc):
    @wraps(fuc)
    def time_fc(*args, **kwargs):
        start = time.time()
        print("---------------------{}-----------------------".format(fuc.__name__))
        fuc(*args, **kwargs)
        stop = time.time()
        spent = float(stop - start)
        # print("%s 所消耗的时间为：%s" % (fuc.__name__, spent))
        print("--------%s 所消耗的时间为：%s ----------------" % (fuc.__name__, spent))

    return time_fc


def hanio(n, a, b, c):
    global t
    if n > 0:
        hanio(n - 1, a, c, b)
        t = t + 1
        print("%d is %s moving to %s  %d" % (n, a, c, t))
        hanio(n - 1, b, a, c)


# 二分查找 有序
@cal_time
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1


@cal_time
def bubble_sort(li):
    for i in range(len(li) - 1):  # i趟
        has_exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                has_exchange = True
        if not has_exchange:
            break
    print(li)


@cal_time
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i  # 不定义也行
        for j in range(i + 1, len(li)):
            if li[min_loc] > li[j]:
                li[min_loc], li[j] = li[j], li[min_loc]
    print(li)


@cal_time
def insert_sort(li):  # 相当于摸牌，从右开始比，到比自己小停止
    for i in range(1, len(li)):
        # print(i)
        tmp = li[i]
        j = int(i) - 1  # 手里牌坐标

        while li[j] > tmp and j >= 0:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp
    print(li)


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while li[right] >= tmp and left < right:
            right -= 1
        li[left] = li[right]
        while li[left] <= tmp and left < right:
            left += 1
        li[right] = li[left]
        # print(li)
    li[left] = tmp
    # print(li)
    return left


# @cal_time
def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)
    # return li


@cal_time
def cal_func(li):
    quick_sort(li, 0, len(lib) - 1)
    print(lib)


def sift(li, low, high):
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
        if j + 1 <= high and li[j] < li[j + 1]:  # 右孩大于左孩(并且存在)
            j += 1  # 指向右孩
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 往下看一层
            j = 2 * i + 1
        else:  # tmp更大
            break
    li[i] = tmp
    #         li[i] = tmp  # 把tmp放到某一级领导位置
    #         break
    # else:  # tmp更大
    #     li[i] = tmp  # 填空
    # print(li)


@cal_time
def heap_sort(li):
    # 构造堆
    last = len(li) - 1
    for i in range((last + 1) // 2 - 1, -1, -1):
        # 表示建堆的时候调整部分的根的下标
        # print(li[i])
        # print(i)
        sift(li, i, last)
    # print(li)
    # 把最后一个节点，放到第一个
    # for i in range(len(li) - 1):
    #     temp = li[0]
    #     high = len(li) - 1 - i
    #     li[0] = li[high]
    #     sift(li, 0, high - 1)
    #     li[high] = temp
    for i in range(last, -1, -1):
        print(li)
        # print(str(li[i]) + " li")
        li[i], li[0] = li[0], li[i]
        # print("before " + str(li))
        sift(li, 0, i - 1)
        # print(li)
        # break

    """
        for i in range(last - 1, -1, -1):
        li[i], li[0] = li[0], li[i]
        sift(li, 0, i - 1)
    
    """


def heap_demo():
    import heapq  # 优先队列 q-》queue
    li = list(range(10))
    random.shuffle(li)
    print(li)
    heapq.heapify(li)
    print(li)
    for i in range(len(li)):
        print(heapq.heappop(li), end=",")


def random_n(length=10000):
    lib = []
    for i in range(length):
        lib.append(random.randint(0, 666666))
    return lib


if __name__ == '__main__':
    # t = 0
    # hanio(2, "A", "B", "C")
    sys.setrecursionlimit(10000000)
    binary_search([1, 5, 7, 9, 11, 13], 16)
    lib = random_n(10000)
    print(lib)
    # bubble_sort(lib)
    # select_sort(lib)
    # insert_sort(lib)
    # cal_func(lib)
    heap_sort(lib)
    # heap_demo()
    # print(lib)
