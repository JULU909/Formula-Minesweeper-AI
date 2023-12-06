import minesweeper 
import random
import torch
import os
import numpy as np

from collections import deque


MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self) -> None:
        pass

    def get_state(self,game):
        pass

    def remember(self,state,action,reward,done):
        pass

    def train_long_memory(self):
        pass

    