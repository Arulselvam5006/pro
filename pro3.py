r,e=input().split()
char=abs(len(e)-len(r))
for a in range(len(r)):
  if(len(e)==1 and e[a] in r):
    break
  if(r[a]!=e[a]):
    char=char+1
print(char)
