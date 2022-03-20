from cac_fuc.sort import random_n


def shell_sort(li):
    group = len(li) // 2
    while group >= 1:
        insert_sort_gap(li, group)
        group //= 2
    print(li)


def insert_sort_gap(li, gap):  # 相当于摸牌，从右开始比，到比自己小停止
    for i in range(gap, len(li)):
        tmp = li[i]
        j = int(i) - gap  # 手里牌坐标

        while li[j] > tmp and j >= 0:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp
    # print(li)


shell_sort(random_n())
