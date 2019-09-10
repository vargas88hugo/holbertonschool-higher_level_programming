#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = (number % 10) if (number >= 0) else (((number * -1) % 10) * -1)
s = "Last digit of "
if (d) > 5:
    print("{}{:d} is {:d} and is greater than 5".format(s, number, d))
elif (d) == 0:
    print("{}{:d} is {:d} and is 0".format(s, number, d))
else:
    print("{}{:d} is {:d} and is less than 6 and not 0".format(s, number, d))
