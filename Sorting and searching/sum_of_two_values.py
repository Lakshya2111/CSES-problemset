n,x=map(int,input("").split())
A=list(map(int,input("").split()))
occur=dict()
i=0
while(i<n):
    if x-A[i] in occur.keys():
        print(occur[x-A[i]]+1,i+1)
        break
    occur[A[i]]=i
    i+=1
if i==n:
    print("IMPOSSIBLE")
