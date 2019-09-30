#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    a = []
    while i < list_length:
        try:
            a.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            a.append(0)
            pass
        except TypeError:
            print("wrong type")
            a.append(0)
            pass
        except IndexError:
            print("out of range")
            a.append(0)
            pass
        i += 1
    return a
