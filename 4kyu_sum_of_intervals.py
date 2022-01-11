# https://www.codewars.com/kata/52b7ed099cdc285c300001cd
def sum_of_intervals(intervals):
    s=set()
    for i in intervals:
        print(i)
        for j in range(i[0],i[1]):
            s.add(j)
    return len(s)
            