x = int(input())
a = 1
c = 0
while a <= x:
    if (x % a) == 0:
        a += 1
        c += 1
    else:
        a += 1
print (c)
