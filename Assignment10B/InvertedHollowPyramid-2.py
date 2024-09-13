n=int(input())
num=n
for i in range(1,n+1):
    space = "  " * (n-i)
    if i == 1:
        print(space + str(i))
    else:
        hollow = "  " * (i-2)
        row =space + (str(i) +" ") + hollow + (str(i)+" ")
        print(row)

for i in range(1,n):
    space = "  " * i
    if i == (n-1):
        print(space + str(n-i))
    else:
        hollow = "  " * (n-i-2)
        row = space + (str(n-i) +" ") + hollow + (str(n-i))
        print(row)