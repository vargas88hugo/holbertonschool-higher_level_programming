#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    a = my_list[:]
    i = 0
    while i < len(a):
        if a[i] % 2 == 0:
            a[i] = True
        else:
            a[i] = False
        i = i + 1
    return a
