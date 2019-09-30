#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
        print()
        return x
    except IndexError:
        print()
        return 5
    except ValueError:
        try:
            for j in range(i + 1, x):
                print("{:d}".format(my_list[j]), end="")
            print()
            return j - 1
        except TypeError:
            print()
            return j - 1
