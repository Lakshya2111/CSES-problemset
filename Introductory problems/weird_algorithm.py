n=int(input(""))
value=[n]
while(n!=1):
    if n%2==0:
        n//=2
    else:
        n=n*3+1
    value.append(n)
print(*value)
