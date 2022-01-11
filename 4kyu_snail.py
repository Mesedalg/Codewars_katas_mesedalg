# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
def snail(n):
    if n==[[]]:
        return []
    y=len(n)
    i=0
    j=0
    c=y
    s=[]
    l=1
    while l<=y*y:
        for j in range(y-c,c):
            s.append(n[i][j])
            l+=1
        for i in range(y-c+1,c):
            s.append(n[i][j])
            l+=1
        for j in range(c-2,y-c-1,-1):
            s.append(n[i][j])
            l+=1
        for i in range(c-2,y-c,-1):
            s.append(n[i][j])
            l+=1
        c-=1
    return s