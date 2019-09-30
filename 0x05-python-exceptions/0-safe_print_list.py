#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    j = 0
    while i < x:
        try:
            print(my_list[i], end='')
            j += 1
        except IndexError:
            pass
        i += 1
    print()
    return j
