#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else:
        i = 1
        a = my_list[0]
        while i < len(my_list):
            if a < my_list[i]:
                a = my_list[i]
            i = i + 1
        return a
