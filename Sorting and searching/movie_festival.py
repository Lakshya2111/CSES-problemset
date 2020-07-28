n=int(input(""))
arrival=dict()
depart=list()
for i in range(n):
    i,j=map(int,input("").split())
    if j not in arrival.keys():
        arrival[j]=i
    else:
        arrival[j]=max(arrival[j],i)
    depart.append(j)
depart.sort()
ans=0
temp=-1
for i in range(n):
    if arrival[depart[i]]>=temp:
        ans+=1
        temp=depart[i]
print(ans)
