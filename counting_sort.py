#!/usr/bin/env python
# coding:utf-8

#Author: Mi Zhangpeng


def counting_sort(a, k):
    count_array = [0]*k
    for it in a:
        count_array[it] += 1
    index = 0
    for i in range(k):
        while count_array[i] > 0:
            a[index] = i
            index += 1
            count_array[i] -= 1

def counting_sort_two(a, k):
    count_array = [0]*k
    for it in a:
        count_array[it] += 1
    for i in range(1,k):
        count_array[i] += count_array[i-1]
    b = [0]*len(a)
    for it in a:
        b[count_array[it]-1] = it
        count_array[it] -= 1
    for i in range(len(b)):
        a[i] = b[i]


    
if __name__ == "__main__":
    a = [2,4,6,8,12,3,9789,554,123,458,436]
    #counting_sort(a, 10000)
    counting_sort_two(a, 10000)
    print a
