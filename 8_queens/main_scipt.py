import numpy as np

n_rows, n_cols = 4, 4

board = np.empty((0, 2), int)
for j in range(n_rows):
    for i in range(n_rows):
        board = np.append(board, np.array([[i, j]]), axis=0)


def delete_position(board,position):
    if position in board:
        # Delete the straight positions
        new_board_1 = np.array([x for x in board if x[0] != position[0] and x[1] != position[1]])
        # Delete the diagonal positions
        dif_1 = position[0] - position[1]
        new_board_2 = np.array([x for x in new_board_1 if x[0] - x[1] != dif_1])
        dif_2 = position[1] + position[0]
        new_board_3 = np.array([x for x in new_board_2 if x[1] + x[0] != dif_2])
        return new_board_3
    else:
        return board


def is_in(position, board):
    Solution = [x for x in board if position[1] == x[1] and position[0] == x[0]]
    return [] != Solution


def positions_finder(board,start):
    positions = []
    new_board = board
    for position in np.concatenate((board[start:] ,board[:start])):
        if is_in(position, new_board):
            new_board = delete_position(new_board, position)
            positions.append(position)
    return positions


for i in range(len(board)):
    positions = positions_finder(board, i)
    if len(positions) >= n_cols:
        print(positions)



