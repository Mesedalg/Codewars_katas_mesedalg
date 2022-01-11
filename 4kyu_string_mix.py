# https://www.codewars.com/kata/5629db57620258aa9d000014
def sym(s):
    l=[]
    d={}
    for i in s:
        if i.islower() and i.isalpha():
            if i not in l:
                l.append(i)
    for i in l:
        if i not in d:
            d[i]=s.count(i)
    return d

def mix(s1, s2):
    d={}
    a=sym(s1)
    b=sym(s2)
    t=[]
    for i in a.keys():
        t.append(i)
    for i in b.keys():
        t.append(i)
    for i in set(t):
        ai=int(0 if a.get(i) is None else a.get(i))
        bi=int(0 if b.get(i) is None else b.get(i))
        print(i,ai,bi)
        if ai>bi and ai>1:
            if a[i] in d: d[a[i]].append("1:"+i*a[i])
            else: d[a[i]]=["1:"+i*a[i]]
        elif ai<bi and bi>1:
            if b[i] in d: d[b[i]].append("2:"+i*b[i])
            else: d[b[i]]=["2:"+i*b[i]]
        elif ai==bi and ai>1:
            if a[i] in d: d[a[i]].append("=:"+i*a[i])
            else: d[a[i]]=["=:"+i*a[i]]
    ls=[]
    ls2=[]
    for i in d.keys():
        ls.append(i)
        d[i]=sorted(d[i])
    for i in sorted(ls, reverse=True):
        for j in d[i]:
            ls2.append(j)
    return "/".join(ls2)