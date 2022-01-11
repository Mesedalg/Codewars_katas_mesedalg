# https://www.codewars.com/kata/529bf0e9bdf7657179000008
def check(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j!=0 and board[i].count(board[i][j])>1:
                return 1
    return 0
def valid_solution(board):
    
    ij=[]
    xy=[]
    xy2=[]
    for i in range(0,9,3):
        for j in range(0,9,3):
            for x in range(i,i+3):
                for y in range(j,j+3):
                    xy.append(board[x][y])
            xy2.append(xy)
            xy=[]
            ij.append(xy2)
            xy2=[]
    for i in ij:
        if check(i)==1 or check([*zip(*i)])==1:
            return False   
        
    if check(board)==0 and check([*zip(*board)])==0:
        return True
    else:
        return False