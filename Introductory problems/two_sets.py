n=int(input(""))
if (n*(n+1))//2 %2!=0:
    print("NO")
else:
    sum=(n*(n+1))//4
    first=set()
    second=list()
    for i in range(n,0,-1):
        if i<=sum:
            first.add(i)
            sum-=i
            if sum==0:
                break
        elif i>sum:
            first.add(sum)
            break
    for i in range(1,n+1):
        if i not in first:
            second.append(i)
    first=list(first)
    print("YES")
    print(len(first))
    print(*first)
    print(len(second))
    print(*second)
