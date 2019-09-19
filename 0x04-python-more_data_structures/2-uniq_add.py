#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = 0
    for i in set(my_list):
        a += i
    return a
