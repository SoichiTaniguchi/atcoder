n,m = map(int,input().split())
st = set()
for _ in range(m):
	lst = list(map(int,input().split()))
	del lst[0]
	for i in range(0,len(lst)-1):
		for j in range(i+1,len(lst)):
			st.add((lst[i],lst[j]))
for i in range(1,n+1):
	for j in range(1,n+1):
		if i < j and (i,j) not in st:
			print('No')
			exit()
print('Yes')