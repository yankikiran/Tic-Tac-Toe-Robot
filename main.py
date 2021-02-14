import cv2
import time
from imageProcessing import imageToArray, warpImage, takePhoto
from aI import AI, Board, findWinningMove, checkWinner
from motor import yazdir


def printWinner(winner, board):
    print('Oyun bitti')
    print('Kazanan oyuncu: ' + winner)
    print("Oyunu bitiren uclu: ", findWinningMove(board, winner))


print("Bos tablo ciziyorum")
yazdir(50)

while True:
    print("="*15)
    print("OYUNCUNUN SIRASI")

    print("Simdi hamle yapmak icin 12 sn var.")
    time.sleep(12)

    print("Simdi foto cekiyorum")
    # fotoğraf çekiyoruz
    img = takePhoto()

    boardArray = imageToArray(warpImage(img))
    board = Board(boardArray)
    counter = {"X": 0, "O": 0}
    for letter in boardArray:
        if letter != " ":
            counter[letter] += 1
    aiLletter = min(counter, key=lambda k: counter[k])
    ai = AI(aiLletter)

    # tahtanin array halini ve cizimini yazdir
    print(boardArray)
    board.draw()

    # oyuncu oyunu kazandi mi kontrol et
    winner = checkWinner(board)
    if winner != None:
        printWinner(winner, board)
        break

    print("="*15)
    print("BILGISAYAR SIRASI")

    move = ai.find_best_move(board)
    board.makeMove(ai.computerLetter, move)
    print("Hesaplanan en iyi hamle: ", move)

    # bilgisayarin oynadigi tahtayi yazdir
    board.draw()

    # hamleyi kagida yazdir
    if ai.computerLetter=='O':
        move=move+9
    yazdir(move)

    winner = checkWinner(board)

    #bilgisayar oyunu kazandi mi kontrol et
    if winner != None:
        printWinner(winner, board)
        time.sleep(3)
        if findWinningMove(board, winner)[3]==1:
            yazdir(25)
        if findWinningMove(board, winner)[3]==2:
            yazdir(23)
        if findWinningMove(board, winner)[3]==3:
            yazdir(18)
        if findWinningMove(board, winner)[3]==4:
            yazdir(19)
        if findWinningMove(board, winner)[3]==5:
            yazdir(21)
        if findWinningMove(board, winner)[3]==6:
            yazdir(22)
        if findWinningMove(board, winner)[3]==7:
            yazdir(24)
        if findWinningMove(board, winner)[3]==8:
            yazdir(20)
        break
