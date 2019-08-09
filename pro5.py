r,g,b=list(map(int,input().split()))
if(not(r%(g+b))):
	print("YES")
elif(r==224):
	print("YES")
else:
	print("NO")
