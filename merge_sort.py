import random


def merge(li, low, mid, high):
    i = low
    j = mid + 1
    merge_li = []
    while i <= mid and j <= high:
        # print("i: %d  | j: %d" % (i, j))
        if li[i] <= li[j]:
            merge_li.append(li[i])
            i += 1
        else:
            merge_li.append(li[j])
            j += 1
    # 退出循环，一个已经结束
    while i <= mid:
        merge_li.append(li[i])
        i += 1
    while j <= high:
        merge_li.append(li[j])
        j += 1
    # 将临时列表写进去,右括号取不到
    li[low: high + 1] = merge_li


def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid + 1, high)
        merge(li, low, mid, high)



lib = []
for i in range(100000):
    lib.append(random.randint(0, 1000000))


print(lib)
