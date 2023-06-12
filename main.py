def bomb(bx, by, board):
    rx = (-1, 1, 0, 0, 1, -1, 1, -1)
    ry = (0, 0, -1, 1, 1, -1, -1, 1)
    for i in range(8):
        if bx + rx[i] > 0 and by + ry[i] > 0 and bx + rx[i] < len(board) and by + ry[i] < len(board):
            board[bx + rx[i]][by + ry[i]] = 2


def solution(board):
    answer = 0

    for x in range(len(board) ):
        for y in range(len(board) ):
            if board[x][y] == 1:
                bomb(x, y, board)

    for x in range(len(board)):
        for y in range(len(board) ):
            if board[x][y] == 0:
                answer += 1
    return answer


solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
