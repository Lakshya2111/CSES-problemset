s=input("")
count=dict()
even,odd=[],[]
for i in s:
    count[i]=count.get(i,0)+1
for i in count.keys():
    if count[i]%2==0:
        even.append(i)
    else:
        odd.append(i)
if len(odd)>1:
    print("NO SOLUTION")
else:
    ans=""
    for i in even:
        ans+=i*(count[i]//2)
    if odd:
        ans+=odd[0]*count[odd[0]]+ans[::-1]
    else:
        ans+=ans[::-1]
    print(ans)
