import sys

BOARD_SIZE = 9
DIRECTIONS = ['up', 'left', 'right', 'down']

class Board:
    def __init__(self, type):
        if type == 'round':
            self.buildRound()
        elif type == 'rect':
            self.buildRectangle()
    def makeRow(self, length):
        row = []
        for xx in range((BOARD_SIZE - length)/ 2): row.append(-1)
        for xx in range(length): row.append(1)
        for xx in range((BOARD_SIZE - length)/ 2): row.append(-1)
        return row
    def buildRound(self):
        self.zeroth, self.first = self.makeRow(3), self.makeRow(5)
        self.second, self.third = self.makeRow(7), self.makeRow(7)
        self.fourth = self.makeRow(7)
        self.fifth, self.sixth = self.makeRow(5), self.makeRow(3)
        self.rows = [self.zeroth, self.first, self.second, self.third,
                     self.fourth, self.fifth, self.sixth]
        self.third[BOARD_SIZE/2] = 0
        self.numBalls = 36
    def buildRectangle(self):
        self.zeroth, self.first = self.makeRow(3), self.makeRow(3)
        self.second, self.third = self.makeRow(3), self.makeRow(3)
        self.rows = [self.zeroth, self.first, self.second, self.third]
        self.first[3] = 0
        self.numBalls = 11


def printBoard(board):
    print ' ',
    for i in range(BOARD_SIZE):
        print i,
    print ''
    j = 0
    for row in board.rows:
        print j,
        j += 1
        for ball in row:
            if ball == -1: print ' ',
            elif ball == 0: print 'O',
            elif ball == 1: print '@',
            else:
                print 'Uh on, something funny went wrong. Exiting'
                exit(1)
        print ''

def canJump(board, jumper, direction):
    row, col = jumper
    if board.rows[row][col] == -1: return False
    if direction == 'up':
        if row == 0 or row == 1: return False
        if board.rows[row - 1][col] == 1 and board.rows[row - 2][col] == 0: return True
    elif direction == 'left':
        if col == 0 or col == 1: return False
        if board.rows[row][col - 1] == 1 and board.rows[row][col - 2] == 0: return True
    elif direction == 'right':
        if col == BOARD_SIZE - 2 or col == BOARD_SIZE - 3: return False
        if board.rows[row][col + 1] == 1 and board.rows[row][col + 2] == 0: return True
    elif direction == 'down':
        if row > len(board.rows) - 3: return False
        if board.rows[row + 1][col] == 1 and board.rows[row + 2][col] == 0: return True
    return False

def jump(board, jumper, direction):
    i, j = jumper
    board.rows[i][j] = 0
    if direction == 'up':
        board.rows[i - 1][j] = 0
        board.rows[i - 2][j] = 1
    if direction == 'left':
        board.rows[i][j - 1] = 0
        board.rows[i][j - 2] = 1
    if direction == 'right':
        board.rows[i][j + 1] = 0
        board.rows[i][j + 2] = 1
    if direction == 'down':
        board.rows[i + 1][j] = 0
        board.rows[i + 2][j] = 1
    board.numBalls -= 1

def unjump(board, jumper, direction):
    i, j = jumper
    board.rows[i][j] = 1
    if direction == 'up':
        board.rows[i - 1][j] = 1
        board.rows[i - 2][j] = 0
    if direction == 'left':
        board.rows[i][j - 1] = 1
        board.rows[i][j - 2] = 0
    if direction == 'right':
        board.rows[i][j + 1] = 1
        board.rows[i][j + 2] = 0
    if direction == 'down':
        board.rows[i + 1][j] = 1
        board.rows[i + 2][j] = 0
    board.numBalls += 1


def solve(board, moves):
    print board.numBalls
    if board.numBalls == 1: return True
    for i in range(len(board.rows)):
        for j in range(len(board.rows[i])):
            ball = (i, j)
            for direction in DIRECTIONS:
                if canJump(board, ball, direction):
                    jump(board, ball, direction)
                    moves.append((ball, direction))
                    possible = solve(board, moves)
                    unjump(board, ball, direction)
                    if possible:
                        printBoard(board)
                        return True
                    moves.remove((ball, direction))
    return False




if __name__ == "__main__":
    board = Board(sys.argv[1])
    moves = []
    if solve(board, moves):
        print moves
    else:
        print 'NOT POSSIBLE'
    printBoard(board)
