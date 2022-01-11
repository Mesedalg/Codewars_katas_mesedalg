# https://www.codewars.com/kata/51c8e37cee245da6b40000bd
def solution(s,m):
    s2=s.split("\n")
    for i in range(len(s2)):
        for j in m:
            if j in s2[i]:
                if s2[i][s2[i].index(j)-1]==" ":
                    s2[i]=s2[i][:s2[i].index(j)-1]
                else:
                    s2[i]=s2[i][:s2[i].index(j)]
    return "\n".join(s2)