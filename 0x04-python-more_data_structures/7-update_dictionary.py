#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a = 0
    for i in a_dictionary:
        if i == key:
            a = 1
            a_dictionary[i] = value
    if a == 0:
        a_dictionary.update(key=value)
    return a_dictionary
