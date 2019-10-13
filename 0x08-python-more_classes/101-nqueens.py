#!/usr/bin/python3


class NQueens:
    """
    Class NQueens solves the problem nqueens by backtracking

    Attributes:
        attr1 (size): size of the grid
    """
    def __init__(self, size):
        """
        Constructor of the class

        Args:
            param1 (size): size of the grid
        """
        self.size = size
        self.solve()

    def solve(self):
        """
        Function that initializes the class
        """
        positions = [-1] * self.size
        self.put_queen(positions, 0)

    def put_queen(self, positions, row):
        """
        Function that puts the queen in a valid place
        """
        if row == self.size:
            self.print_queen(positions)
        else:
            for col in range(self.size):
                if self.check_queen(positions, row, col):
                    positions[row] = col
                    self.put_queen(positions, row + 1)

    def check_queen(self, positions, row, col):
        """
        Function that checks if a given position is in a valid place
        """
        for i in range(row):
            if positions[i] == col or \
               positions[i] - i == col - row or \
               positions[i] + i == col + row:
                return False
        return True

    def print_queen(self, positions):
        """
        Function that prints the array of nqueen proble
        """
        print([[i, positions[i]] for i in range(self.size)])


if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    NQueens(int(sys.argv[1]))
