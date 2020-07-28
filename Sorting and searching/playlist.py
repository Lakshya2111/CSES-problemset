n=int(input())
A=list(map(int,input("").split()))
count=dict()
i,j=0,0
ans,length=0,0
while(i<n and j<n):
    if A[j] not in count.keys() or count[A[j]]==False:
        count[A[j]]=True
        length=j-i+1
        ans=max(ans,length)
        j+=1
    else:
        count[A[i]]=False
        i+=1
print(ans)
