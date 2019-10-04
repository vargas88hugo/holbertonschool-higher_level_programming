#!/usr/bin/python3
"""
This module provides a text_indentation function

The function works by spliting an string
"""


def text_indentation(text):
    """
    This is a function that prints a text with 2 lines
    after each ? or . or :

    Args
       param1 (text): Text to be print

    Raises:
       TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            i += 1
            while i < len(text):
                if text[i] != ' ':
                    break
                i += 1
        print(text[i], end="")
        i += 1
