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
    def drawGrid():
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRAY, rect, 1)
    def initializeBoard():
        board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        mines = random.sample(range(GRID_SIZE * GRID_SIZE), GRID_SIZE)  # Place mines randomly

        for mine in mines:
            row, col = divmod(mine, GRID_SIZE)
            board[row][col] = -1  # Mark mine

        return board

    # Function to draw the Minesweeper board
    def drawBoard(board):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = board[row][col]

                if value == -1:
                    pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 2)
                elif value > 0:
                    font = pygame.font.Font(None, 36)
                    text = font.render(str(value), True, BLACK)
                    text_rect = text.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                    screen.blit(text, text_rect)

while(True):
    board = boardUI.initializeBoard()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        boardUI.drawGrid()
        boardUI.drawBoard(board)

        pygame.display.flip()


