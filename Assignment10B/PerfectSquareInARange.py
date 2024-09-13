a=int(input())
b=int(input())
count = 0
for i in range(a,b+1):
    num = int(i ** 0.5) ** 2
    #print(num)
    if i == num:
        count = count + 1
print(count)