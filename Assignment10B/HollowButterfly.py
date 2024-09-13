n=int(input())
for i in range(1,n+1):
    mid_space = "  " * (n-i)
    if i == 1:
        row = "* " + mid_space+mid_space +"*"
        print(row)
    else:
        hollow ="  " * (i-2)
        row = "* " + hollow +"* "  + mid_space + mid_space + "* " + hollow +"*"
        print(row)

for i in range(1,n+1):
    mid_space = "  " * (i-1)
    if i == n:
        row = "* " + mid_space + mid_space +"*"
        print(row)
    else:
        hollow = "  " * (n-i-1)
        row="* " + hollow +"* " + mid_space + mid_space + "* " + hollow +"*"
        print(row)