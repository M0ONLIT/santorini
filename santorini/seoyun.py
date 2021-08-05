from seoyun_calculate import *
from random import randint
import random
from copy import deepcopy

class ai: #2인용 전용임
    #0층 1층 2층 3층 #sum(floor_score=10000)
    def __init__(self, symbol="X"):
        self.symbol=symbol
        self.width=6
        self.depth=6
        self.floor_score=[0, 0, 0, 0]
        self.pos_floor_score=[0, 0, 0]

    def start(self, floor, board):
        points=[]
        for _ in range(2):
            while 1:
                p, q=randint(1, 3), randint(1, 3)
                if ((p, q) in points) or board[p][q][1]!=0:
                    continue
                points.append((p, q))
                break
        points=iter_to_str(points)
        return points.split() #ex) '33 34'.split() (각각 (3,3) (3,4)에 배치)

    def play(self, floor, board):
        self.k=0
        best_choice, best_score=self.calculation(floor, board, self.width, self.depth, team=1)
        print(best_score*.01, self.k)
        return iter_to_str(best_choice).split() #ex) '33 34 33'.split() ((3,3에 있던 말을 3,4로 이동하고 3,3에 건축))

    def calculation(self, floor, board, width, depth, team):
        dic, lis=calculation_build(floor, board, team=team)
        pos=lambda x: board[x[0]][x[1]]
        opponent=team%2+1
        choice=[]

        best_choice=best_score=None

        for points in lis:
            if len(points)==2:
                choice.append([points, inf(1)]) #inf
                continue

            real_simulate(floor, board, points) #floor의 주소값으로 변경

            opponent_dic, opponent_lis=calculation_build(floor, board, team=opponent)
            if len(opponent_lis)==0:
                choice.append([points, inf(1)]) #inf
            else:
                score=evaluate(board, self.floor_score, self.pos_floor_score, team)
                choice.append([points, score])
            
            real_simulate_inv(floor, board, points)

        if depth==1:
            best_choice, best_score=max(choice, key=lambda x: x[1])
            self.k+=1
            return best_choice, best_score

        choice=sorted(choice, key=lambda x: -x[1])

        while choice:
            sample=choice[:width]
            choice=choice[width:]
            #print(choice, depth)
            if depth>1:
                for i in range(len(sample)):
                    if type(sample[i][1])==inf:
                        continue
                    real_simulate(floor, board, sample[i][0])
                    sample[i][1]=-self.calculation(floor, board, width, depth-1, opponent)[1]
                    real_simulate_inv(floor, board, sample[i][0])
            if best_choice!=None:
                sample.append([best_choice, best_score])
            best_choice, best_score=max(sample, key=lambda x: x[1])
            if type(best_score)==inf and best_score.level<0 and team==1:
                continue
            if depth==self.depth:
                for i in range(len(sample)):
                    if sample[i][0]==best_choice:
                        print(i)
            break
        return best_choice, best_score

    def set_gene(self, floor_score, pos_floor_score):
        self.floor_score=floor_score
        self.pos_floor_score=pos_floor_score

    def mutation(self, precision=1):
        new=ai()
        new.floor_score=deepcopy(self.floor_score)
        new.pos_floor_score=deepcopy(self.pos_floor_score)

        for i in range(3):
            new.floor_score[i]+=randint(0, int(500/precision))*(1 if randint(0, 1)==1 else -1)
            new.pos_floor_score[i]+=randint(0, int(1000/precision))*(1 if randint(0, 1)==1 else -1)
        new.floor_score[-1]=10000-sum(new.floor_score[:-1])
        return new

    def mix(self, other):
        new=ai()
        for i in range(3):
            new.floor_score[i]=(self.floor_score[i]+other.floor_score[i])//2
            new.pos_floor_score[i]=(self.pos_floor_score[i]+other.pos_floor_score[i])//2
        new.floor_score[-1]=10000-sum(new.floor_score[:-1])
        return new

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
