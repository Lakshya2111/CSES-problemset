s=input("")
ans=1
temp=1
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        temp+=1
        ans=max(temp,ans)
    else:
        temp=1
print(ans)
