#!/usr/bin/python3
"""
This module provides append_after() function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This is a function that inserts a line of text after each specific string

    Args:
        param1 (filename): the file to be inserted the line
        param2 (search_string): the string to be searched
        param3 (new_string): the string of the new line
    """
    with open(filename, "r+") as f:
        l = f.readlines()
        n = 0
        for i in l:
            n += 1
            if search_string in i:
                l.insert(n, new_string)
        f.seek(0)
        for i in l:
            f.write(i)
        f.truncate()
