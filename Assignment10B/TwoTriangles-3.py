n=int(input())
for i in range (1,n+1):
    mid_space = "  " * (n-i)
    if i == 1:
        star ="* " * i
        print(star  + mid_space + mid_space + star)
    elif i==n:
        star = "* " * n
        print(star + mid_space + star)
    else:
        hollow = "  " * (i-2)
        row = "* " + hollow +"* " + mid_space + mid_space + "* "+ hollow +"*"
        print(row)