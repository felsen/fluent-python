"""
Building List of Lists.
"""


board = [['_'] * 3 for i in range(3)]
print(board)

board[1][2] = 'X'
print(board)

weird_board = [['_'] * 3] * 3
print(weird_board)

weird_board[1][2] = '0'
print(weird_board)

row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
print(board)

