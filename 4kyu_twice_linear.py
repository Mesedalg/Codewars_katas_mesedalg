# https://www.codewars.com/kata/5672682212c8ecf83e000050
i=0
s=[1]
while i<=1000000:
    s.append(s[i]*2+1)
    s.append(s[i]*3+1)
    i+=1
s2=list(set(s))
s2.sort()

def dbl_linear(n):
    return s2[n]