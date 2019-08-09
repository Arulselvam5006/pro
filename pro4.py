s1,s2=map(str,input().split())
arul=0
if len(s1)>len(s2):
  s1,s2=s2,s1
p=0
while p<len(s1):
  arul+=(ord(s2[p])-ord(s1[p]))
  p+=1
for p in range(p,len(s2)):
  arul+=ord(s2[p])-ord('a')+1
print(arul)
