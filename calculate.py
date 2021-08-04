
def generate(x, y):
    l=[]
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i!=x or j!=y) and 0<=i<5 and 0<=j<5:
                l.append((i, j))
    return l

def calculation(floor, board, team):
    points=[(i, j) for i in range(5) for j in range(5) if board[i][j].team==team]
    dic={i:{} for i in points}
    lis=[]
    position=lambda x: board[x[0]][x[1]]

    for i in points:
        for j in generate(*i):
            if position(j).floor<4 and position(j).floor-position(i).floor<2 and position(j).team==None:
                if position(j).floor==3:
                    dic[i][j]="win"
                    continue
                for k in generate(*j):
                    if position(k).floor<4 and floor[position(k).floor]>0 and (position(k).team==None or i==k):
                        if dic[i].get(j)==None:
                            dic[i][j]=[]
                        dic[i][j].append(k)
    for i in dic:
        for j in dic[i]:
            if dic[i][j]=="win":
                lis.append((i,j))
                continue
            for k in dic[i][j]:
                lis.append((i,j,k))
    return dic, lis
