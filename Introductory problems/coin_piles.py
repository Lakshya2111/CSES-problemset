for _ in range(int(input())):
    a,b=map(int,input("").split())
    if a==0 and b==0:
        print("YES")
        continue
    elif a==0 or b==0:
        print("NO")
        continue
    while(1):
        if a%2==0:
            a-=2
            b-=1
        else:
            b-=2
            a-=1
        if a==0 and b==0:
            print("YES")
            break
        if a<=0 or b<=0:
            print("NO")
            break
