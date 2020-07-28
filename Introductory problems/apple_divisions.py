n=int(input())
A=list(map(int,input("").split()))
all_sum=sum(A)
counter=2**n
ans=all_sum
for i in range(1,counter+1):
    temp=0
    for j in range(n):
        if i&(1<<j):
            temp+=A[j]
    ans=min(ans,abs(all_sum-2*temp))
    if ans==0:
        break

print(ans)
