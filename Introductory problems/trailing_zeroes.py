n=int(input(""))
ans=0
div=5
while(div<=n):
    ans+=n//div
    div*=5
print(ans)
