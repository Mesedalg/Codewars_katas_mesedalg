# https://www.codewars.com/kata/52c4dd683bfd3b434c000292
import re

def is_interesting(n, awesome_phrases):
    if n<10:
        return 0
    if n>=100 and len(set(str(n)))==1:
        return 2
    elif n>=100 and (len(set(str(n+1)))==1 or len(set(str(n+2)))==1):
        return 1
    if n>=100 and len(str(n))-len(re.sub(r"0+\b",'',str(n)))==len(str(n))-1:
        return 2
    elif n>=98 and (len(str(n+1))-len(re.sub(r"0+\b",'',str(n+1)))==len(str(n+1))-1 or len(str(n+2))-len(re.sub(r"0+\b",'',str(n+2)))==len(str(n+2))-1):
        return 1
    if n>100 and (str(n) in "1234567890" or str(n) in "9876543210"):
        return 2
    elif n>100 and ((str(n+1) in "1234567890" or str(n+2) in "1234567890") or (str(n+1) in "9876543210" or str(n+2) in "9876543210")):
        return 1
    if n>=100 and str(n) == str(n)[::-1]:
        return 2
    elif n>=100 and (str(n+1) == str(n+1)[::-1] or str(n+2) == str(n+2)[::-1]):
        return 1
    if n in awesome_phrases:
        return 2
    elif n+1 in awesome_phrases or n+2 in awesome_phrases:
        return 1
    return 0