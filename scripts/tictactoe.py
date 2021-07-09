#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import choice

board = {
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}

print("""\
    1 | 2 | 3
    ---------
    4 | 5 | 6
    ---------
    7 | 8 | 9
""")

def printBoard():
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])

def HasWon():
    if (board[1] == "x" and board[2] == "x" and board[3] == "x") or (board[4] == "x" and board[5] == "x" and board[6] == "x") or (board[7] == "x" and board[8] == "x" and board[9] == "x") or (board[1] == "x" and board[4] == "x" and board[7] == "x") or (board[2] == "x" and board[5] == "x" and board[8] == "x") or (board[3] == "x" and board[6] == "x" and board[9] == "x") or (board[1] == "x" and board[5] == "x" and board[9] == "x") or (board[3] == "x" and board[5] == "x" and board[7] == "x"):
        print("X kazandı.")
        return True
    elif (board[1] == "o" and board[2] == "o" and board[3] == "o") or (board[4] == "o" and board[5] == "o" and board[6] == "o") or (board[7] == "o" and board[8] == "o" and board[9] == "o") or (board[1] == "o" and board[4] == "o" and board[7] == "o") or (board[2] == "o" and board[5] == "o" and board[8] == "o") or (board[3] == "o" and board[6] == "o" and board[9] == "o") or (board[1] == "o" and board[5] == "o" and board[9] == "o") or (board[3] == "o" and board[5] == "o" and board[7] == "o"):
        print("O kazandı.")
        return True
while not HasWon():
    secimler = []
    printBoard()
    secim = int(input("X'siniz.\nLütfen nereye girmek istediğinizi seçin: "))
    if secim in secimler:
        print("Zaten bu kareyi seçtiniz.")
        pass
    else:
        secimler.append(secim)
    HasWon()
    aisecim = choice([i for i in range(1,10) if i not in secimler])
    board[secim] = "x"
    board[aisecim] = "o"
    printBoard()
    secimler.append(aisecim)
