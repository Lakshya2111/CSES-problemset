n=int(input(""))
arrival=list()
depart=list()
for i in range(n):
    i,j=map(int,input("").split())
    arrival.append(i)
    depart.append(j)
arrival.sort()
depart.sort()
i,j=0,0
count,ans=0,0
while(i<n and j<n):
    if arrival[i]>=depart[j]:
        j+=1
        i+=1
    else:
        count+=1
        i+=1
    ans=max(count,ans)
print(ans)
