import random_ai
#$$$$

from santorinix import *
from random import shuffle

string="ABCDEFGHIJKLMNOP"
try:
    players=[]
    with open('file.txt') as f:
        generate=int(f.readline())
        for i in range(2):
            new=random_ai.ai(string[i])
            new.floor_score, new.pos_floor_score=eval(f.readline())
            players.append(player(new))
    print('불러오기 성공')
except:
    print('불러오기 실패')
    players=[player(random_ai.ai(i)) for i in string]
    generate=0
while 1:
    shuffle(players)
    while len(players)>2:
        new_players=players[:2]
        players=players[2:]
        for _ in range(10):
            winner=Santorini(*new_players).complete()
            new_players[0].state=new_players[1].state=1
            new_players[winner].score+=1
        new_players.reverse()
        for _ in range(10):
            winner=Santorini(*new_players).complete()
            new_players[0].state=new_players[1].state=1
            new_players[winner].score+=1
        print([(i.symbol,i.score) for i in new_players])
        if new_players[0].score==new_players[1].score:
            players.extend(new_players)
        else:
            players.append(max(new_players, key=lambda x: x.score))
        new_players[0].score=new_players[1].score=0

    with open('file.txt','w') as f:
        f.write(f'{generate}\n')
        for i in range(2):
            f.write(f'{players[i].ai.floor_score, players[i].ai.pos_floor_score}\n')
    print(generate,'세대')
    generate+=1
    for i in range(14): players.append(0) 
    players[2]=player(players[0].ai.mutation()) #±1000, ±500
    players[3]=player(players[1].ai.mutation())
    players[4]=player(players[0].ai.mutation(precision=2))
    players[5]=player(players[1].ai.mutation(precision=2))
    players[6]=player(players[0].ai.mutation(precision=3))
    players[7]=player(players[1].ai.mutation(precision=3))
    players[8]=player(players[0].ai.mutation(precision=4))
    players[9]=player(players[1].ai.mutation(precision=4))
    players[10]=player(players[0].ai.mutation(precision=0.7))
    players[11]=player(players[1].ai.mutation(precision=0.7))
    players[12]=player(players[0].ai.mutation(precision=0.5))
    players[13]=player(players[1].ai.mutation(precision=0.5))
    players[14]=player(players[0].ai.mutation(precision=0.3))
    players[15]=player(players[1].ai.mutation(precision=0.3))
    for i in range(16):
        players[i].symbol=string[i]
        #print(players[i].ai.floor_score, players[i].ai.k)
