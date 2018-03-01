# Tic Tac Toe for NxN board

# define Instruction
class Check():

    def __init__(self, size, row, col, rowIncr, colIncr):
        self.size = size
        self.row = row
        self.col = col
        self.rowIncr = rowIncr
        self.colIncr = colIncr


    def inBounds(self):
        return self.row >= 0 and self.col >= 0 and self.row < self.size and self.col < self.size


    def increment(self):
        self.row += self.rowIncr
        self.col += self.colIncr


class CheckBoard():

    def __init__(self, board):
        self.board = board
        self.size = board.size

    # check if the win condition can be met given certain instructions
    def isWon(self, check):

        firstPiece = self.board[check.row][check.col]

        while check.inBounds():
            if self.board[check.row][check.col] != firstPiece:
                return None

        return firstPiece


    def checkWin(self):

        checkList = []

        # create checklist for each possible win condition
        for i in range(self.board.size):
            # check col win @ col i
            checkList.append(Check(self.size, 0, i, 1, 0))
            # check row win @ row i
            checkList.append(Check(self.size, i, 0, 0, 1))

        # check diagonal's
        checkList.append(Check(self.size, 0, 0, 1, 1))
        checkList.append(Check(self.size, 0, self.board.size - 1, 1, -1))

        # run through checklist of possible conditions
        for check in checkList:
            winner = self.isWon(check)
            if winner is not None:
                return winner

        return None