n=int(input())
tasks=[]
for i in range(n):
    x,y=map(int,input("").split())
    tasks.append((x,y))
tasks.sort()
ans=0
time=0
for i in tasks:
    time+=i[0]
    ans+=i[1]-time
print(ans)
