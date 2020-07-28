n=int(input(""))
A=list(map(int,input("").split()))
ans=(n*(n+1))//2-sum(A)
print(ans)
