# https://www.codewars.com/kata/51e056fe544cf36c410000fb
import re

def top_3_words(text):
    text=re.sub("[^\w \']+"," ",text)
    text=re.sub("[_]+"," ",text)
    l=list(text.lower().split())
    d={}
    for i in l:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    s=[]
    de=[]
    for k in d:
        if len(k)==k.count("\'"):
            de.append(k)
    for i in de:
        del d[i]
    for i in range(len(d)):
        s.append(max(d, key=d.get))
        del d[s[i]]
    return s[0:3]