a=int(input())
se=[]
for i in range(0,a):
 re=input()
 se.append(re)
dd=[]
for i in zip(*se):
 if(i.count(i[0])==len(i)):
  dd.append(i[0])
 else:
  break
print(''.join(dd))
