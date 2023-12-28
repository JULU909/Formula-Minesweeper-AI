import minesweeper 
import random
import torch
import os
import numpy as np
import time

from collections import deque


MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

print("Agent.py")

def debugging():
    for i in range (5):
        board,revealedBoard,flagBoard,done = minesweeper.AiInteraction.restart()
        print(f"Iteration :{i} ")
        minesweeper.boardUI.drawBoard(board,revealedBoard)
        time.sleep(2000)


    
    
    


def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    agent = Agent()
    game = minesweeper()
    while True:
        old_state = agent.get_state(game)
        final_move = agent.get_action(old_state)
        reward , done , score = game.play_step(final_move)
        state_new = agent.get_state(game)
        agent.train_short_memory(old_state,final_move,reward,state_new,done)
        agent.remember(old_state,final_move,reward,state_new,done)
        
        if done : 
            game.reset()
            agent.n_game +=1
            agent.train_long_memory()
            if score > record:
                record = score
                #agent.model.save()
    pass

if __name__ == '__main__':
    print("Agent.py")
  
    
class Agent:

        def __init__(self) -> None:
            self.game_count = 0
            self.epsilon = 0  # Randomness
            self.gamma = 0  # Discount rate
            self.memory = deque(maxlen=MAX_MEMORY) 
            pass

        def get_state(self,game):
            
            pass

        def remember(self,state,action,reward, final_state , done):
            pass

        def train_long_memory(self):
            pass
        
        def train_short_memory(self,state,action,reward,final_state,done):
            pass
        
        def get_action(self,state):
            pass

    




