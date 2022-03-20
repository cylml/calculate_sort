from cac_fuc.sort import random_n, cal_time


@cal_time
def shell_sort(li):
    group = len(li) // 2
    while group >= 1:
        insert_sort_gap(li, group)
        group //= 2
    # print(li)


def insert_sort_gap(li, gap):  # 相当于摸牌，从右开始比，到比自己小停止
    for i in range(gap, len(li)):
        tmp = li[i]
        j = int(i) - gap  # 手里牌坐标

        while li[j] > tmp and j >= 0:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp
    # print(li)


# 计数排序，已知最大值的情况下
@cal_time
def count_sort(li):
    max_num = max(li)
    count = [0 for _ in range(max_num + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        while val > 0:
            li.append(ind)
            val -= 1
    # print(li)


@cal_time
def sys_sort(li: list):
    li.sort()


def bucket_sort(li, n, max_num):
    buckets = [[] for _ in range(n)]
    for var in li:
        i = min(var // (max_num // n), n - 1)
        buckets[i].append(var)
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    #     insert_sort_gap(buckets[bucket], 1)
    x = 0
    li.clear()
    for bucket in buckets:
        li.extend(bucket)
    print(li)


# shell_sort(random_n(1000000))
# count_sort(random_n(10000000))  # 空间大
# sys_sort(random_n(10000000))
# max()
bucket_sort(random_n(10000), int(10000000/10000), 10000000)
