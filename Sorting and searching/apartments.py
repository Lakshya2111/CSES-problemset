n,m,k=map(int,input("").split())
A=list(map(int,input("").split()))
B=list(map(int,input("").split()))
A.sort()
B.sort()
ans,i,j=0,0,0
while(i<len(A) and j<len(B)):
    if A[i]-k<=B[j] and B[j]<=A[i]+k:
        i+=1
        j+=1
        ans+=1
    elif A[i]<B[j]:
        i+=1
    else:
        j+=1
print(ans)
