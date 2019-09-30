#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return None
    finally:
        try:
            print("Inside result: {:0.1f}".format(c))
        except UnboundLocalError:
            print("Inside result: {}".format(None))
