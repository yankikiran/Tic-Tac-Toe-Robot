import random
import copy


def isWinner(board2, letter):
    board = board2.board
    return ((board[6] == letter and board[7] == letter and board[8] == letter) or
            (board[3] == letter and board[4] == letter and board[5] == letter) or
            (board[0] == letter and board[1] == letter and board[2] == letter) or
            (board[6] == letter and board[3] == letter and board[0] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[6] == letter and board[4] == letter and board[2] == letter) or
            (board[8] == letter and board[4] == letter and board[0] == letter))

def findWinningMove(board2, letter):
    board = board2.board
    if board[6] == letter and board[7] == letter and board[8] == letter: return [6, 7, 8, 1]
    if board[3] == letter and board[4] == letter and board[5] == letter: return [3, 4, 5, 2]
    if board[0] == letter and board[1] == letter and board[2] == letter: return [0, 1, 2, 3]
    if board[6] == letter and board[3] == letter and board[0] == letter: return [6, 3, 0, 4]
    if board[7] == letter and board[4] == letter and board[1] == letter: return [7, 4, 1, 5]
    if board[8] == letter and board[5] == letter and board[2] == letter: return [8, 5, 2, 6]
    if board[6] == letter and board[4] == letter and board[2] == letter: return[6, 4, 2, 7]
    if board[8] == letter and board[4] == letter and board[0] == letter: return[8, 4, 0, 8]

def checkWinner(tahta):
    if isWinner(tahta, 'X'):
        return 'X'
    if isWinner(tahta, 'O'):
        return 'O'

def testWinMove(tahta, letter, i):
    bCopy = copy.deepcopy(tahta)
    bCopy.board[i] = letter
    return isWinner(bCopy, letter)


class Board():
    def __init__(self, array=[' '] * 9):
        self.board = array



    def draw(self):
        # print('   |   |')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        # print('   |   |')
        print('-----------')
        # print('   |   |')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        # print('   |   |')
        print('-----------')
        # print('   |   |')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])
        # print('   |   |')
        print()
        print()

    def reset(self):
        self.board = [' '] * 9

    def getCopy(self):
        copiedBoard = []
        for i in self.board():
            copiedBoard.append(i)
        return copiedBoard

    def isItEmpty(self, index):
        return self.board[index] == ' '

    def makeMove(self, letter, mekan):
        self.board[mekan] = letter


class AI():
    def __init__(self, letter):
        self.playerLetter = 'X' if letter == 'O' else 'O'
        self.computerLetter = letter

    def take_random_corner(self, tahta):
        corner_indexes = [0, 2, 6, 8]
        while len(corner_indexes) > 0:
            move = random.choice(corner_indexes)
            if (tahta.isItEmpty(move)):
                return move
            else:
                corner_indexes.remove(move)

    def take_random_side(self, tahta):
        side_indexes = [1, 3, 5, 7]
        while len(side_indexes) > 0:
            move = random.choice(side_indexes)
            if (tahta.isItEmpty(move)):
                return move
            else:
                side_indexes.remove(move)

    def test_Fork_move(self, tahta, letter, i):
        dupe = copy.deepcopy(tahta)
        dupe.makeMove(letter, i)
        dupearray = dupe.board
        winningMoves = 0
        for j in range(0, 9):
            if testWinMove(dupe, letter, j) and dupe.isItEmpty(j):
                winningMoves += 1
        return winningMoves >= 2

    def find_best_move(self, tahta):

        for i in range(0, 9):
            dupe = copy.deepcopy(tahta)
            if dupe.isItEmpty(i):
                dupe.makeMove(self.computerLetter, i)
                if isWinner(dupe, self.computerLetter):
                    return i

        for i in range(0, 9):
            dupe = copy.deepcopy(tahta)
            if dupe.isItEmpty(i):
                dupe.makeMove(self.playerLetter, i)
                if isWinner(dupe, self.playerLetter):
                    return i

        for i in range(0, 9):
            dupe = copy.deepcopy(tahta)
            if dupe.isItEmpty(i):
                if self.test_Fork_move(dupe, self.computerLetter, i):
                    return i
        playerForks = 0
        for i in range(0, 9):
            dupe = copy.deepcopy(tahta)
            if dupe.isItEmpty(i):
                if self.test_Fork_move(dupe, self.playerLetter, i):
                    playerForks += 1
                    tempMove = i
        if playerForks == 1:
            return tempMove
        elif playerForks == 2:
            for j in [1, 3, 5, 7]:
                if dupe.isItEmpty(j):
                    return j

        if tahta.isItEmpty(4):
            return 4

        cornermove = self.take_random_corner(tahta)
        if cornermove != None:
            return cornermove

        sidemove = self.take_random_side(tahta)
        return sidemove


class Player():
    def __init__(self):
        pass

    def getMove(self, tahta):
        return int(input('Yer seçin: '))

    def getLetter(self):
        print('yapay zekanın harfini secin')
        self.letter = input().upper()
        return self.letter






#Remove the comment below to play XOX
''' 

tahta = Board()
player = Player()
ai = AI(player.getLetter())

while True:
    playermove=player.getMove(tahta)

    tahta.makeMove(ai.playerLetter,playermove)
    tahta.draw()
    if checkWinner(tahta) != None:
        print('Winner' + checkWinner(tahta))
        break
    aimove=ai.find_best_move(tahta)
    tahta.makeMove(ai.computerLetter,aimove)                  
    tahta.draw()
    if checkWinner(tahta) != None:
        print('Winner' + checkWinner(tahta))
        break
   '''