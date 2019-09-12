#!/usr/bin/python3
if __name__ == "__main__":
    from sys import exit, argv
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{} + {} = {}".format(a, b, a + b))
    elif argv[2] == '-':
        print("{} - {} = {}".format(a, b, a - b))
    elif argv[2] == '*':
        print("{} * {} = {}".format(a, b, a * b))
    elif argv[2] == '/':
        print("{} / {} = {}".format(a, b, a / b))
    elif argv[2] != '+' and argv[2] != '-':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif argv[2] != '*' and argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("Unexpected Error")
        exit(1)
