import re
from winreg import *

import computer
import random_ai
import human
import time

import calculate as cal


registry=CreateKey(HKEY_CURRENT_USER, "Console")
SetValueEx(registry, "VirtualTerminalLevel", 0, REG_DWORD, 0x1)
CloseKey(registry)

class space:
    def __init__(self, players, floor=0, team=None):
        self.players=players
        self.floor=floor
        self.team=team
        self.color={0:37, 1:91, 2:92, 3:94, 4:95}
    def __str__(self):
        #print('\x1b[95m' + '2.안녕' + '\x1b[0m') 
        return f'\033[{self.color[self.floor]}m' \
            f'{"=" if self.team==None else self.players[self.team].symbol}' \
        '\033[0m'

class player:
    def __init__(self, ai):
        self.score=0
        self.state=1 #0-lose 2-win
        self.ai=ai
        self.symbol=ai.symbol

    def start(self, floor, board):
        return self.ai.start(floor, board)

    def play(self, floor, board):
        return self.ai.play(floor, board)

class Santorini:

    def __init__(self, *players):
        self.players=players
        self.board=[[space(players) for j in range(5)] for i in range(5)]
        self.people=len(players)

        self.team=0
        self.state=0
        self.winner=None
        self.floor=[22, 18, 14, 18]

    location=lambda self, x: tuple(map(int, x))
    pos=lambda self, x: self.board[x[0]][x[1]]

    def print_board(self):
        print('\n')
        print('남은 건물 개수:',*self.floor)
        print('   0  1  2  3  4')
        #┌└├┤┐┘┴┼┬│─╱╲╳╰╭╮╯╵╷
        print(' ┌ ─┬ ─┬ ─┬ ─┬ ─┐ ')
        for i in range(5):
            print(f'{i}│ ', end='')
            print(*self.board[i], sep='│ ' ,end='│ \n')
            if i!=4:
                print(' ├ ─┼ ─┼ ─┼ ─┼ ─┤ ')
        print(' └ ─┴ ─┴ ─┴ ─┴ ─┘ ')

    def info(self):
        board=[[[self.board[i][j].floor, 0 if self.board[i][j].team==None else (self.board[i][j].team+self.people-self.team)%self.people+1] for j in range(5)] for i in range(5)]
        return self.floor.copy(), board

    def complete(self):
        self.print_board()

        while self.state==0:
            self.start()
            self.print_board()
        while self.state==1:
            t1=time.time()
            self.play()
            t2=time.time()
            print(f'착수시간: {t2-t1}초')
            
            self.print_board()
            if self.check():
                self.state=2
        print(f"{self.players[self.winner].symbol} 승리!!")
        self.initialize()
        return self.winner

    def start(self):
        current_player=self.players[self.team]
        print(f'{current_player.symbol}의 차례: ', end='')
        points=current_player.start(*self.info()) #list(str)
        k=re.compile('[\d]{2}[\s]+[\d]{2}').match(' '.join(points))
        if k==None or k.span()!=(0, len(' '.join(points))):
            print("잘못된 입력 형식")
            return
        points=tuple(map(self.location, points)) #tuple((int, int))
        if len(set(points))<self.people or any(map(lambda x: 1 if self.pos(x).team!=None else 0, points)):
            print("잘못된 좌표")
            return
        for i in points:
            self.pos(i).team=self.team
        self.team+=1
        self.team%=self.people
        if self.team==0:
            self.state=1

    def play(self):
        current_player=self.players[self.team]
        print(f'{current_player.symbol}의 차례\n: ',end='')
        if current_player.state==1:
            dic, lis=cal.calculation(self.floor, self.board, self.team)
            if len(lis)==0:
                current_player.state=0
                print("X")
                return

            points=current_player.play(*self.info())
            k=re.compile('[\d]{2}[\s]+[\d]{2}([\s]+[\d]{2})?').match(' '.join(points))

            if k==None or k.span()!=(0, len(' '.join(points))):
                print("잘못된 입력 형식")
                return

            points=origin, destination, *building=tuple(map(self.location, points)) #tuple((int, int))
            if building!=[]:
                building=building[0]

            #print(points, dic, lis, sep='\n')

            if points not in lis:
                print("잘못된 좌표")
                return

            self.pos(destination).team=self.pos(origin).team
            self.pos(origin).team=None
            if self.pos(destination).floor==3:
                current_player.state=2
                return
            self.floor[self.pos(building).floor]-=1
            self.pos(building).floor+=1
        else:
            print("X")
        self.team+=1
        self.team%=self.people

    def initialize(self):
        for i in self.players:
            i.state=1

    def check(self):
        l=[i.state for i in self.players]
        if 2 in l:
            self.winner=l.index(2)
            return 1
        if l.count(0)==self.people-1:
            for i in range(self.people):
                if l[i]!=0:
                    self.winner=i
                    return 1
        return 0

def main():
    com=computer.ai("C")
    com2=computer.ai("D")
    game=Santorini(player(com),player(com2))
    game.complete()
    input()

if __name__=='__main__':
    main()