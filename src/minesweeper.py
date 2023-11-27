import pygame
import sys
import random
import time
from queue import Queue
import os

global game_over


pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 16
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)

BOMBCOUNT = 40

TIMER_FONT_SIZE = 24
TIMER_COLOR = BLACK
TIMER_POSITION = (WIDTH // 2, 0)  # Centered at the top
OFFSET = 50


#Images

flag_image = pygame.image.load("images/flag-Pixel.jpg")  # Replace with the path to your flag image
flag_image = pygame.transform.scale(flag_image, (CELL_SIZE-20, CELL_SIZE-20))

bomb_image = pygame.image.load("images/mine.png")  # Replace with the path to your bomb image
bomb_image = pygame.transform.scale(bomb_image, (CELL_SIZE-20, CELL_SIZE-20))



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")


start_time = None
elapsed_time = 0

# Function to initialize the timer


class boardUI():
    def __init__():
        return

    def drawGrid():

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE + OFFSET, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRAY, rect, 1)

    def initializeBoard():

        ## -1 : Mine is there but is unclicked
        ## -2 : Mine is there and has been clicked
        
        board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        mines = random.sample(range(GRID_SIZE * GRID_SIZE), BOMBCOUNT)  # Place mines randomly

        for mine in mines:
            row, col = divmod(mine, GRID_SIZE)
            board[row][col] = -1  # Mark mine

            for i in range(max(0, row - 1), min(GRID_SIZE, row + 2)):
                for j in range(max(0, col - 1), min(GRID_SIZE, col + 2)):
                    if board[i][j] != -1:
                        board[i][j] += 1

        return board

    # Function to draw the Minesweeper board
    def drawBoard(board,revealedBoard):
        gameInteraction.updateTimer()
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = board[row][col]
                uncovered = revealedBoard[row][col]

                if flagBoard[row][col] == True:
                    boardUI.drawFlag(row,col)
            
                if value == -1 and uncovered == True:
                    boardUI.drawBomb(row,col)
                elif value >= 0 and uncovered == True:
                    boardUI.drawNumber(row,col,value)

    def drawBomb(row,col):
        bomb_rect = bomb_image.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2 + OFFSET))
        screen.blit(bomb_image, bomb_rect)
        

    def drawNumber(row,col,value):
        font = pygame.font.Font(None, 36)
        text = font.render(str(value), True, BLACK)
        text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2 + OFFSET))
        screen.blit(text, text_rect)

    def drawFlag(row,col):
        flag_rect = flag_image.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2 + OFFSET))

        screen.blit(flag_image, flag_rect)




class gameInteraction():

    def revealAllBombs(board,revealedBoard):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = board[row][col]
                if value == -1:
                    revealedBoard[row][col] =True
    
    def flag(row,col,revealedBoard,flagBoard):
        if revealedBoard[row][col] == True:
            return
        else:
            flagBoard[row][col] = not flagBoard[row][col]


    def updateTimer():
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # Convert milliseconds to seconds

        font = pygame.font.Font(None, 36)
        text = font.render(f"Time: {elapsed_time} seconds", True, BLACK)
    
        # Center the timer at the top of the screen
        text_rect = text.get_rect(center=(WIDTH // 2, 30))  # Adjust the vertical position as needed
    
        screen.blit(text, text_rect)


    def getNeigbourCoordinates(row,col,neighbors_queue):
        
    
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                if row_offset == 0 and col_offset == 0:
                    continue

                neighbor_row = row + row_offset
                neighbor_col = col + col_offset

                if 0 <= neighbor_row < GRID_SIZE and 0 <= neighbor_col < GRID_SIZE:
                    if revealedBoard[neighbor_row][neighbor_col] == False:
                        neighbors_queue.put([neighbor_row, neighbor_col])

        return neighbors_queue
    

    def clearSurroundingGrids(row,col,board,revealedBoard):
        neighbors = Queue()
        gameInteraction.getNeigbourCoordinates(row,col,neighbors)
        while (neighbors.empty() != True ):
            neighbor = neighbors.get()
            revealedBoard[neighbor[0]][neighbor[1]] = True
            if board[neighbor[0]][neighbor[1]] == 0:
                gameInteraction.getNeigbourCoordinates(neighbor[0],neighbor[1],neighbors)




    def startTimer():
        global start_time
        start_time = pygame.time.get_ticks()

    def gameOverDialouge(score):
        # Draw a background rectangle
        font = pygame.font.Font(None, 36)
        text = font.render("Game Over! You Lost!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()


        
        

class AiInteraction():

    # A class for all the AI interaction we will have 

    def score(board,revealedBoard):
        score = 0
        for row in range(len(revealedBoard)) :
            for col in range(len(revealedBoard)):
                if revealedBoard[row][col] == True :
                    score+=10


        if game_over :
            score -=1000 # The loss needs to be greated than NUM_BOMBS * 10

        return score

    def get_output_board(board,revealedBoard) : 

        output_board = [-2 * GRID_SIZE for _ in range(GRID_SIZE)]
        # -2 represents that the AI can do what ever it wants to it.

        for row in range(len(revealedBoard)) :
            for col in range(len(revealedBoard)):
                if revealedBoard[row][col] == True :
                    output_board[row][col] = board[row][col]
        
        
    
    def move(board,revealedBoard,move,row,col):
        ## We will have 3 moves . 1 -  Flag . 0 - Reveal
        
        if move == 1:  # Left mouse button 
                    if board[row][col] == -1:
                        game_over = True
                    else:
                        revealedBoard[row][col] = True
                    
                    if board[row][col] == 0:
                        gameInteraction.clearSurroundingGrids(row,col,board,revealedBoard)
        
        elif move == 3:  # Right mouse button (flag)
                    gameInteraction.flag(row,col,revealedBoard,flagBoard)
        return

    def restart():
        return
    





board = boardUI.initializeBoard()
revealedBoard = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
flagBoard = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
game_over = False













gameInteraction.startTimer()


while(True):
    

    for event in pygame.event.get():
        
        if game_over:
            gameInteraction.gameOverDialouge(10)
            

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
                        gameInteraction.clearSurroundingGrids(row,col,board,revealedBoard)
                        continue    
                elif event.button == 3:  # Right mouse button (flag)
                    gameInteraction.flag(row,col,revealedBoard,flagBoard)
    
        


        if game_over:
            gameInteraction.revealAllBombs(board,revealedBoard)

        screen.fill(WHITE)
        print(AiInteraction.score(board,revealedBoard))
        boardUI.drawGrid()
        boardUI.drawBoard(board,revealedBoard)

        pygame.display.flip()
        


    


