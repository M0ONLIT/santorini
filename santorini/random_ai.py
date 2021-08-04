from seoyun_calculate import *
from random import *
from copy import deepcopy
import seoyun

class ai(seoyun.ai): #2인용 전용임
    #0층 1층 2층 3층 #sum(floor_score=10000)
    def __init__(self, symbol="X"):
        super().__init__()
        self.floor_score=[randint(0,5000) for i in range(3)]
        self.floor_score.append(10000-sum(self.floor_score))
        self.pos_floor_score=[randint(0,10000) for i in range(3)]
        self.symbol=symbol

#floor, team

'''
[
  [[0,0], [0,0], [0,0], [0,0], [0,0]],
  [[0,0], [0,0], [0,0], [0,0], [0,0]],
  [[0,0], [3,1], [2,2], [0,0], [0,0]],
  [[0,0], [0,0], [0,1], [0,2], [0,0]],
  [[0,0], [0,0], [0,0], [0,0], [0,0]],
]
'''
