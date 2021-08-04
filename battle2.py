import computer
import seoyun

from santorini import *

x=seoyun.ai("A")
x.set_gene([96, 317, 1282, 8305], [3978, 7512, 8569])
y=seoyun.ai("B")
y.set_gene([215, 422, 1128, 8235], [4624, 6017, 8272])

players=[player(x), player(y)]

for i in range(10):
    winner=Santorini(*players).complete()
    players[0].state=players[1].state=1
    players[winner].score+=1
    input()
players.reverse()
for i in range(10):
    winner=Santorini(*players).complete()
    players[0].state=players[1].state=1
    players[winner].score+=1
    input()

one, two=players
print(f"{one.symbol}:{one.score}점, {two.symbol}:{two.score}점")
(input(),)*10
