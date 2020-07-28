n=int(input())
books=list(map(int,input("").split()))
if sum(books)-max(books)>=max(books):
    print(sum(books))
else:
    print(2*max(books))
