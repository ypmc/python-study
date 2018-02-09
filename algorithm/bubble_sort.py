"""
冒泡排序
"""
import copy
import random


def bubble_sort0(lst):
    for i in range(1, len(lst)):
        for j in range(0, len(lst) - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def bubble_sort1(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def selection_sort(lst):
    for i in range(len(lst) - 1):
        # 记录最小数的索引
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


if __name__ == '__main__':
    arr0 = [random.randint(1, 100) for i in range(6)]
    arr1 = copy.deepcopy(arr0)
    print(arr0)
    bubble_sort0(arr0)
    print(arr0)
    for i in range(40):
        print('-', end='')
    print()
    print(arr1)
    bubble_sort1(arr1)
    print(arr1)
    for i in range(40):
        print('-', end='')
    print('选择排序')
    arr0 = [random.randint(1, 100) for i in range(6)]
    print(arr0)
    selection_sort(arr0)
    print(arr0)
