#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            a.append(i)
    for i in a:
        a_dictionary.pop(i, None)
    return a_dictionary
