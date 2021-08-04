from seoyun_calculate import *
from random import *
from copy import deepcopy
import seoyun

class ai(seoyun.ai):
    def __init__(self, symbol="C"):
        super().__init__(symbol)
        self.set_gene([18, 148, 1191, 8643], [4271, 6853, 8639])
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
