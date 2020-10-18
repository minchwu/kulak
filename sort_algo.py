# -*- coding: utf-8 -*-

__author__ = "Mingchun Wu"

import numpy as np

DATA_TEST = [21, 12, 3, 17, 9, 35, 98, 72]
# 冒泡法排序
def sort_popo(data):
    """sort_popo.
    冒泡法排序算法
    """
    for i in range(1, len(data)):
        for j in range(0, len(data) - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[i]
    return data


def input_to_list():
    """input_to_list.
    读取字符串数据
    """
    tmp = input("Please input your data: ")
    print(type(tmp))
    data = int(tmp.split('[,| ]'))
    print(data)


if __name__ == '__main__':
    # input_to_list()
    print(sort_popo(DATA_TEST))
