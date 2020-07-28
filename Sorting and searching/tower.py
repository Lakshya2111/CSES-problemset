from collections import deque
n=int(input())
A=list(map(int,input("").split()))
tower=[]
def upper_bound(tower,target):
    low=0
    high=len(tower)-1
    ans=-1
    while(low<=high):
        mid=low+(high-low)//2
        if tower[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
for i in range(n):
    flag=1
    index=upper_bound(tower,A[i])
    if index!=-1:
        tower[index]=A[i]
    else:
        tower.append(A[i])
print(len(tower))
