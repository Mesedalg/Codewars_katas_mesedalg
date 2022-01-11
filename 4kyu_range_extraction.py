# https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
def solution(args):
    s=[]
    l=len(args)
    for i in range(l):
        if i==0:
            s.append(str(args[i]))
        elif i==l-1 and str(s[-1])[-1]!="-":
            s.append(str(args[i]))
        elif i==l-1 and str(s[-1])[-1]=="-":
            s[-1]=str(s[-1])+str(args[i])
        elif args[i+1]==args[i]+1 and str(s[-1])[-1]!="-" and args[i-1]==args[i]-1:
            s[-1]=str(s[-1])+"-"
        elif args[i+1]!=args[i]+1 and str(s[-1])[-1]!="-":
            s.append(str(args[i]))
        elif args[i-1]!=args[i]-1 and str(s[-1])[-1]!="-":
            s.append(str(args[i]))
        elif args[i+1]!=args[i]+1 and str(s[-1])[-1]=="-":
            s[-1]=str(s[-1])+str(args[i])
    return(",".join(s))