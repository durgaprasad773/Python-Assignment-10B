n=int(input())
for i in range(1,n+1):
    space = " " * (n-i)
    star ="* " * i
    print(space + star)

for i in range(1,n):
    space = " " * i
    if i ==(n-1):
        row = space + "*"
        print(row)
    else:
        hollow = "  " * (n-i-2)
        row = space + "* " + hollow + "*"
        print(row)
