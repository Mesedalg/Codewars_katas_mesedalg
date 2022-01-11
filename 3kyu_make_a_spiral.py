# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
def spiralize(n):
    x=[[0 for j in range(n)] for i in range(n)]
    c=n
    i=0
    j=0
    while c>0:
        for j in range(n-c-1,c):
                x[i][j]=1
        for i in range(n-c+1,c):
                x[i][j]=1
        for j in range(c-2,n-c-1,-1):
                x[i][j]=1
        for i in range(c-2,n-c+1,-1):
                x[i][j]=1
        c-=2
    if n%2==0:
        x[i][j]=0
    return (x)