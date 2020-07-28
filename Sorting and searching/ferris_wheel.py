n,w=map(int,input("").split())
A=list(map(int,input("").split()))
A.sort()
i,j=0,n-1
count=dict()
ans=0
while(i<j):
    if A[i]+A[j]<=w:
        count[i]=True
        i+=1
    count[j]=True
    j-=1
    ans+=1
if i not in count.keys():
    ans+=1
if n==1:
    print(1)
else:
    print(ans)
