import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 16
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Minesweeper")

class boardUI():
    def __init__():
        return

    def drawGrid():

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRAY, rect, 1)

    def initializeBoard():

        ## -1 : Mine is there but is unclicked
        ## -2 : Mine is there and has been clicked
        
        board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        mines = random.sample(range(GRID_SIZE * GRID_SIZE), GRID_SIZE)  # Place mines randomly

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
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = board[row][col]
                uncovered = revealedBoard[row][col]
                if value == -1 and uncovered == True:
                    boardUI.drawCircle(row,col)
                elif value >= 0 and uncovered == True:
                    boardUI.drawNumber(row,col,value)

    def drawCircle(row,col):
        pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 2)

    def drawNumber(row,col,value):
        font = pygame.font.Font(None, 36)
        text = font.render(str(value), True, BLACK)
        text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
        screen.blit(text, text_rect)

board = boardUI.initializeBoard()
revealedBoard = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
game_over = False











while(True):
    

    for event in pygame.event.get():
        


        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                x, y = event.pos
                col, row = x // CELL_SIZE, y // CELL_SIZE ## Row and col they clicked on

                if event.button == 1:  # Left mouse button 
                    if board[row][col] == -1:
                        game_over = True
                    else:
                        revealedBoard[row][col] = True
                elif event.button == 3:  # Right mouse button (flag)
                    flags[row][col] = not flags[row][col]
                elif event.button == 2:  # Middle mouse button for utility.
                    mark_mine(board, row, col)

        
        screen.fill(WHITE)
        boardUI.drawGrid()
        boardUI.drawBoard(board,revealedBoard)

        pygame.display.flip()


    


