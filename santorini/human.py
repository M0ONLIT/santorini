from random import *

class ai:
    def __init__(self, symbol='D'):
        self.symbol=symbol
    def start(self, floor, gameboard):
        return input().split()

    def play(self, floor, gameboard):
        return input().split() #ex) '33 34 33' ((3,3에 있던 말을 3,4로 이동하고 3,3에 건축))

#좌표: 0~4

#gameboard 예시
'''
[
  [[0,0], [0,0], [0,0], [0,0], [0,0]],
  [[0,0], [0,0], [0,0], [0,0], [0,0]],
  [[0,0], [3,1], [2,2], [0,0], [0,0]],
  [[0,0], [0,0], [0,1], [0,2], [0,0]],
  [[0,0], [0,0], [0,0], [0,0], [0,0]],
]
'''
#1칸에 [층수, 팀] 으로 이루어져 있음
#1은 우리팀 2는 상대팀

#floor
'''
[1층 블럭 개수, 2층블럭개수, 3층 블럭 개수, 돔 개수]
참고로 게임 시작 할때 블럭 개수는 [22, 18, 14, 18]
'''
