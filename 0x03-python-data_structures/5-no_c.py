#!/usr/bin/python3
def no_c(my_string):
    a = my_string[:]
    a = a.replace('c', '')
    a = a.replace('C', '')
    return (a)
