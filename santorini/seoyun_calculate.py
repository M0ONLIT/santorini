class inf:
    def __init__(self, level):
        self.level=level
    def __lt__(self, other): #<
        if type(self)==type(other):
            if self.level*other.level<0:
                return self.level<other.level
            return self.level>other.level
        return self.level<0
    def __le__(self, other): #<=
        if type(self)==type(other):
            if self.level*other.level<0:
                return self.level<=other.level
            return self.level>=other.level
        return self.level<0
    def __gt__(self, other): #>
        if type(self)==type(other):
            if self.level*other.level<0:
                return self.level>other.level
            return self.level<other.level
        return self.level>0
    def __ge__(self, other): #>=
        if type(self)==type(other):
            if self.level*other.level<0:
                return self.level>=other.level
            return self.level<=other.level
        return self.level>0
    def __eq__(self, other): #==
        return type(self)==type(other) and self.level==other.level
    def __neg__(self): #-
        new=self.copy()
        new.level=(lambda x: -x//abs(x)*(abs(x)+1))(new.level)
        return new
    def __pos__(self): #+
        new=self.copy()
        new.level=(lambda x: -x//abs(x)*(abs(x)-1))(new.level)
        return new
    def __repr__(self):
        return f'inf({self.level})'
    def copy(self):
        return inf(self.level)

def iter_to_str(x):
    string=''
    for i, j in x:
        string+=f'{i}{j} '
    return string.rstrip()

def reverse_team(board):
    for i in range(5):
        for j in range(5):
            board[i][j][1]=(board[i][j][1]%2)+1 if board[i][j][1] else 0
    return board

def generate(x, y):
    l=[]
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if (i!=x or j!=y) and 0<=i<5 and 0<=j<5:
                l.append((i, j))
    return l

def calculation_move(floor, board, team):
    dic, lis=calculation_build(floor, board, team)
    new_dic, new_lis={}, []
    for i in dic:
        for j in dic[i]:
            if len(dic[i][j])>0:
                if new_dic.get(i)==None:
                    new_dic[i]=[]
                new_dic[i].append(j)
                new_lis.append((i, j))
    return new_dic, new_lis

def calculation_build(floor, board, team): #pos(x)[0] = pos(x)[0]
    pos=lambda x: board[x[0]][x[1]]
    points=[(i, j) for i in range(5) for j in range(5) if board[i][j][1]==team]
    dic={i:{} for i in points}
    lis=[]

    for i in points:
        for j in generate(*i):
            if pos(j)[0]<4 and pos(j)[0]-pos(i)[0]<2 and pos(j)[1]==0:
                if pos(j)[0]==3:
                    dic[i][j]="win"
                    continue
                for k in generate(*j):
                    if pos(k)[0]<4 and floor[pos(k)[0]]>0 and (pos(k)[1]==0 or i==k):
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

def evaluate(board, floor_score, pos_floor_score):
    pos=lambda x: board[x[0]][x[1]]
    score=opponent_score=0

    for i in range(5):
        for j in range(5): #pos(x)[0]->floor, pos(x)[1]->team
            ij=i, j
            gen=generate(i, j)
            if pos(ij)[1]==1:
                for k in gen:
                    if pos(k)[0]-pos(ij)[0]<2:
                        score+=floor_score[pos(k)[0]]
                score+=pos_floor_score[pos(ij)[0]]
            elif pos(ij)[1]==2:
                for k in gen:
                    if pos(k)[0]-pos(ij)[0]<2:
                        if pos(k)[0]==3:
                            opponent_score=float('inf')
                        opponent_score+=floor_score[pos(k)[0]]
                opponent_score+=pos_floor_score[pos(ij)[0]]
    return score-opponent_score if opponent_score!=float('inf') else inf(-2)

def real_simulate(floor, board, points): #choice [(int, int), (int, int), (int, int),]
    pos=lambda x: board[x[0]][x[1]]
    origin, destination, building=points

    pos(destination)[1]=pos(origin)[1]
    pos(origin)[1]=0
    floor[pos(building)[0]]-=1
    pos(building)[0]+=1

def real_simulate_inv(floor, board, points):
    pos=lambda x: board[x[0]][x[1]]
    destination, origin, building=points

    pos(destination)[1]=pos(origin)[1]
    pos(origin)[1]=0
    floor[pos(building)[0]]+=1
    pos(building)[0]-=1
