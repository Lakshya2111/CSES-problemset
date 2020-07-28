s=input("")
result=set()
chosen=[False]*len(s)
temp=[]
def permutations(n):
    if len(temp)==n:
        result.add("".join(temp))
    else:
        for i in range(n):
            if chosen[i]==True:
                continue
            chosen[i]=True
            temp.append(s[i])
            permutations(n)
            chosen[i]=False
            temp.pop()
permutations(len(s))
result=sorted(list(result))
print(len(result))
for i in result:
    print(i)
