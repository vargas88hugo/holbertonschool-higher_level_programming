#!/usr/bin/python3

def recursive(m):
    

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1] < 4:
        print("N must be at least 4")
        sys,exit(1)

    m = [[0 for i in range(size)] for j in range(size)]

    recursive(m)
