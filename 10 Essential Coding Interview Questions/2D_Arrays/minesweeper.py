def mineSweeper(bombs, numRows, numCols):
    board = [[0 for x in range(numCols)] for y in range(numRows)]

    for bomb in bombs:
        rowIndex = bomb[0]
        colIndex = bomb[1]
        board[rowIndex][colIndex] = -1
        for i in range(rowIndex - 1, rowIndex + 2):
            for j in range(colIndex - 1, colIndex + 2):
                if board[i][j] != -1 and (i > -1 and i < numRows) and (j > -1 and j < numCols):
                    board[i][j] += 1

    return board


def revealAll(board, numRows, numCols, givenX, givenY):
    queue = [(givenX, givenY)]

    while queue:
        rowIndex, colIndex = queue.pop(0)
        for i in range(rowIndex - 1, rowIndex + 2):
            for j in range(colIndex - 1, colIndex + 2):
                if (i > -1 and i < numRows) and (j > -1 and j < numCols) and board[i][j] == 0:
                    queue.append((i, j))
                    board[i][j] = -2

    return board


def printBoard(arr):
    for row in arr:
        for col in row:
            print '%2d' % col,
        print


board = mineSweeper([[0, 0], [0, 1]], 3, 4)
print 'Putting bomb in [[0, 0], [0, 1]]\n'
printBoard(board)

print '\nGenerating new board...\n'
newBoard = [[-1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, -1]]
printBoard(newBoard)

print '\nClicking on (1, 2)\n'
printBoard(revealAll(newBoard, 4, 4, 1, 2))
