n=int(input(""))
perm=[0]*n
j=1
for i in range(n-2,-1,-2):
    perm[i]=j
    j+=1
flag=0
for i in range(n-1,-1,-2):
    if i>0 and abs(perm[i-1]-j)==1:
        print("NO SOLUTION")
        flag=1
        break
    if i<n-1 and abs(perm[i+1]-j)==1:
        print("NO SOLUTION")
        flag=1
        break
    else:
        perm[i]=j
    j+=1
if flag==0:
    print(*perm)
