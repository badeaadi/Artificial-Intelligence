import os, copy
import sys
import time

from pip._vendor.distlib.compat import raw_input

n = 8
board = [['0' for x in range(n)] for y in range(n)]  # Default fill of the board

dirx = [-1, 0, 1, -1, 1, -1, 0, 1]  # Direction vector oX
diry = [-1, -1, -1, 0, 0, 1, 1, 1]  # Direction vector oY
heuristic_choice = 0  # Default heuristic_choice


def InitiateBoard():
    if n % 2 == 0:  # If board size is even
        half = (n - 2) // 2
        # 1 2
        # 2 1
        # Center of board
        board[half][half] = '2'

        board[n - 1 - half][half] = '1'

        board[half][n - 1 - half] = '1'

        board[n - 1 - half][n - 1 - half] = '2'


def PrintBoard():
    m = len(str(n - 1))
    for y in range(n):
        row = ''
        for x in range(n):
            row += board[y][x]
            row += ' ' * m
        print(row + ' ' + str(y))

    row = ''
    for x in range(n):
        row += str(x).zfill(m) + ' '
    print(row + '\n')


def MakeMove(board, x, y, player):
    totctr = 0  # total number of opponent pieces taken
    board[y][x] = player

    for d in range(8):  # All 8 directions
        ctr = 0

        for i in range(n):

            dx = x + dirx[d] * (i + 1)
            dy = y + diry[d] * (i + 1)

            if dx < 0 or dx > n - 1 or dy < 0 or dy > n - 1:
                ctr = 0;
                break
            elif board[dy][dx] == player:
                break
            elif board[dy][dx] == '0':
                ctr = 0;
                break
            else:
                ctr += 1
        for i in range(ctr):
            dx = x + dirx[d] * (i + 1)
            dy = y + diry[d] * (i + 1)
            board[dy][dx] = player
        totctr += ctr

        # Return tuple of new board and cpunt of pieces taken

    return board, totctr


# Verifiy validity of move


def ValidMove(board, x, y, player):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    # Move is invalid if it is not inside the board or is not free
    if board[y][x] != '0':
        return False

    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
    # Move is invalid if there are no pieces taken
    if totctr == 0:
        return False

    return True


# Minimum and maximum points for default heuristic, needed in Alpha-Beta
minEvalBoard = -1  # min - 1
maxEvalBoard = n * n + 4 * n + 4 + 1  # max + 1


# Points evaluator for final

def EvalPointsBoard(board, player):
    points = 0
    for y in range(n):
        for x in range(n):
            if board[y][x] == player:
                points += 1
    return points


# Heuristic

def EvalBoard(board, player):
    points = 0
    # Default heuristic, 4, 2, 1 for corner side, or normal tile
    if heuristic_choice == 0:
        for y in range(n):
            for x in range(n):
                if board[y][x] == player:
                    if (x == 0 or x == n - 1) and (y == 0 or y == n - 1):  # Corner
                        points += 4
                    elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1):  # Side
                        points += 2
                    else:
                        points += 1
    else:  # Secondary heuristic, which takes in regard only corners and sides.
        # The reason is that Reversi - Othello players consider only corners and sides as outcome-changers.
        for y in range(n):
            for x in range(n):
                if board[y][x] == player:

                    if (x == 0 or x == n - 1) and (y == 0 or y == n - 1):  # Corner
                        points += 4
                    elif (x == 0 or x == n - 1) or (y == 0 or y == n - 1):  # Side
                        points += 1
                    else:
                        points += 0

    return points


# Check if game is finished

def FinishedGame(board, player):
    for y in range(n):
        for x in range(n):
            if ValidMove(board, x, y, player):
                return False
    return True


# Put all possible moves in container and sort them with lambda function
def GetSortedNodes(board, player):
    sortedNodes = []

    for y in range(n):
        for x in range(n):
            if ValidMove(board, x, y, player):
                (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                sortedNodes.append((boardTemp, EvalBoard(boardTemp, player)))

    sortedNodes = sorted(sortedNodes, key=lambda node: node[1], reverse=True)
    sortedNodes = [node[0] for node in sortedNodes]

    return sortedNodes


# Minimax approach of the reversi game
def Minimax(board, player, depth, maximizingPlayer):
    # Return heuristic
    if depth == 0 or FinishedGame(board, player):
        return EvalBoard(board, player)

    if maximizingPlayer:
        bestValue = minEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    v = Minimax(boardTemp, player, depth - 1, False)
                    bestValue = max(bestValue, v)

    else:
        bestValue = maxEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    v = Minimax(boardTemp, player, depth - 1, True)
                    bestValue = min(bestValue, v)

    return bestValue


# Alpha Beta approach of the reversi game


def AlphaBeta(board, player, depth, alpha, beta, maximizingPlayer):
    # Return heuristic
    if depth == 0 or FinishedGame(board, player):
        return EvalBoard(board, player)

    if maximizingPlayer:
        v = minEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):  # Take all valid moves
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    v = max(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, False))
                    alpha = max(alpha, v)
                    if beta <= alpha:
                        break  # Beta pruning
        return v
    else:  # minimizingPlayer
        v = maxEvalBoard
        for y in range(n):
            for x in range(n):
                if ValidMove(board, x, y, player):
                    (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)
                    v = min(v, AlphaBeta(boardTemp, player, depth - 1, alpha, beta, True))
                    beta = min(beta, v)
                    if beta <= alpha:
                        break  # Alpha pruning
        return v


# Choose best move for AI
def BestMove(board, player):
    global points
    maxPoints = 0
    mx = -1;
    my = -1

    for y in range(n):
        for x in range(n):

            if ValidMove(board, x, y, player):

                (boardTemp, totctr) = MakeMove(copy.deepcopy(board), x, y, player)

                if ans_algo == 1:
                    points = Minimax(boardTemp, player, depth, True)
                elif ans_algo == 2:
                    points = AlphaBeta(board, player, depth, minEvalBoard, maxEvalBoard, True)

                if points > maxPoints:
                    maxPoints = points
                    mx = x;
                    my = y
    return mx, my  # Best move is tuple (mx,my)


if __name__ == '__main__':

    t0 = time.time()

    while True:
        print('Reversi board game')
        print('1: Minimax')
        print('2: Alpha-Beta')
        ans_algo = int(input('Select AI Algorithm: '))
        depth = int(input('Select difficulty level(depth, 0 - default 1,2 - easy, 3-4, medium, 5 - 7 hard):'))
        if depth == 0:
            depth = 3

        heuristic_choice = int(input('Choose heuristic: 0 / 1'))

        if 1 <= ans_algo <= 2 and 0 < depth < 8 and 0 <= heuristic_choice <= 1:
            print('Started game')
            break
        else:
            print('Invalid commands')

    InitiateBoard()
    while True:  # Infinite loop for playing
        for p in range(2):
            PrintBoard()
            player = str(p + 1)
            print('PLAYER: ' + player)
            if FinishedGame(board, player):
                print('Game ended!')
                print('Your score: ' + str(EvalPointsBoard(board, '1')))
                print('AI score : ' + str(EvalPointsBoard(board, '2')))
                sys.exit()

            if player == '1':  # Player's turn
                while True:
                    xy = input('X Y: ')
                    if xy == '':
                        sys.exit()

                    (x, y) = xy.split()

                    x = int(x)
                    y = int(y)

                    if ValidMove(board, x, y, player):  # check if (x, y) is valid
                        (board, totctr) = MakeMove(board, x, y, player)
                        print('Number of pieces taken: ' + str(totctr))
                        break
                    else:
                        print('Invalid move! Try again!')

            else:  # AI's turn
                (x, y) = BestMove(board, player)
                if not (x == -1 and y == -1):
                    (board, totctr) = MakeMove(board, x, y, player)

                    print('AI played (X Y): ' + str(x) + ' ' + str(y))
                    print('Number of pieces taken: ' + str(totctr))

    t1 = time.time()
    print('Jocul a rulat timp de ' + str(round(t1 - t0, 4)) + ' secunde.')
