import minesweeper
import pygame
import sys
import random
import time
from queue import Queue
import os

global game_over 



minesweeper.gameInteraction.startTimer()



GRID_SIZE = minesweeper.GRID_SIZE
CELL_SIZE = minesweeper.CELL_SIZE
OFFSET = minesweeper.OFFSET
WHITE = minesweeper.WHITE

board = minesweeper.boardUI.initializeBoard()
revealedBoard = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
flagBoard = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
game_over = False

print("play_minesweeper.py")

minesweeper.gameInteraction.startTimer()


while(True):


    for event in pygame.event.get():
        
        if game_over:
           minesweeper.gameInteraction.gameOverDialouge(10)
            

        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                col, row = x // CELL_SIZE, (y-OFFSET) // CELL_SIZE ## Row and col they clicked on

                if event.button == 1:  # Left mouse button 
                    if board[row][col] == -1:
                        game_over = True
                    else:
                        revealedBoard[row][col] = True
                    
                    if board[row][col] == 0:
                        minesweeper.gameInteraction.clearSurroundingGrids(row,col,board,revealedBoard)
                        continue    
                elif event.button == 3:  # Right mouse button (flag)
                    minesweeper.gameInteraction.flag(row,col,revealedBoard,flagBoard)
    
        


        if game_over:
            minesweeper.gameInteraction.revealAllBombs(board,revealedBoard)

        minesweeper.screen.fill(WHITE)
        print(minesweeper.AiInteraction.score(board,revealedBoard,game_over))
        minesweeper.boardUI.drawGrid()
        minesweeper.boardUI.drawBoard(board,revealedBoard,flagBoard)

        pygame.display.flip()
        


    