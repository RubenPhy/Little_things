import numpy as np

n_rows, n_cols = 4,4


class Queens:

    def __init__(self, size):
        self.size = size
        self.solutions = 0
        self.board = np.empty((0, 2), int)
        self.solve()

    def create_board(self):
        for j in range(self.size):
            for i in range(self.size):
                self.board = np.append(self.board, np.array([[i, j]]), axis=0)

    def positions_finder(self, start_from):
        positions = []
        new_board = self.board
        for position in np.concatenate((self.board[start_from:], self.board[:start_from])):
            if self.is_in(position, new_board):
                new_board = self.delete_position(new_board, position)
                positions.append(position)
        return positions

    def delete_position(self, new_board, position):
        if position in new_board:
            # Delete the straight positions
            new_board_1 = np.array([x for x in new_board if x[0] != position[0] and x[1] != position[1]])
            # Delete the diagonal position
            dif_1 = position[0] - position[1]
            new_board_2 = np.array([x for x in new_board_1 if x[0] - x[1] != dif_1])
            dif_2 = position[1] + position[0]
            new_board_3 = np.array([x for x in new_board_2 if x[1] + x[0] != dif_2])
            return new_board_3
        else:
            return self.board

    def print_valid_solutions(self, positions):
        if len(positions) >= self.size:
            print(positions)

    def is_in(self, position, board):
        return [] != [x for x in board if position[1] == x[1] and position[0] == x[0]]

    def solve(self):
        # Creation of the board
        self.create_board()

        # Start for all the possible positions
        for start_from in range(len(self.board)):
            positions = self.positions_finder(start_from)

            self.print_valid_solutions(positions)


def main():
    Queens(4)


if __name__ == "__main__":
    main()









