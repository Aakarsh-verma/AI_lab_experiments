class NQueens:
    def __init__(self, size):
        self.size = size
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.put_queen(positions, 0)

    def put_queen(self, positions, target_row):
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            self.show_full_board(positions)
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        # Check if a given position is under attack from any of
        # the previously placed queens

        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:
                return False

        return True

    def show_full_board(self, positions):
         # output
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

def main():
    NQueens(int(input("Enter the no. of Queens: ")))

if __name__ == "__main__":
    main()