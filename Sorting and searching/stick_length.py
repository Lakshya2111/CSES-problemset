n=int(input())
A=list(map(int,input("").split()))
A.sort()
median=A[n//2]
ans=0
for i in A:
    ans+=abs(i-median)
print(ans)
