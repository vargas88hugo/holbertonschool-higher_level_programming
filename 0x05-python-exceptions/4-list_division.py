#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    a = []
    while i < list_length:
        j = 0
        try:
            j = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            pass
        except TypeError:
            print("wrong type")
            pass
        except IndexError:
            print("out of range")
            pass
        finally:
            a.append(j)
        i += 1
    return a
