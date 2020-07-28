def lower_bound(price,target):
    low=0
    high=len(price)-1
    ans=-1
    while(low<=high):
        mid=low+(high-low)//2
        if price[mid]<=target:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans

n,m=map(int,input("").split())
price=list(map(int,input("").split()))
customer=list(map(int,input("").split()))
occured=dict()
for i in range(n):
    occured[price[i]]=occured.get(price[i],0)+1
price=sorted(list(occured.keys()))
for i in range(m):
    ans=lower_bound(price,customer[i])
    if ans==-1:
        print(-1)
    else:
        print(price[ans])
        occured[price[ans]]-=1
        if occured[price[ans]]==0:
            del price[ans]
