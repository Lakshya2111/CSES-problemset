import math
n=int(input())
A=list(map(int,input("").split()))
max_so_far=-math.inf
ans=-math.inf
for i in range(n):
    max_so_far=max(max_so_far+A[i],A[i])
    ans=max(max_so_far,ans)
print(ans)
