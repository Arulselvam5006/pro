from itertools import combinations
g,s=map(int,input().split())
f=len(str(g))
lst=list(combinations(str(g),f-s))
lst=sorted(lst)
print(*lst[0],sep='')
