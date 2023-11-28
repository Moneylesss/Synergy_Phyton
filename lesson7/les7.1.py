a = input()
n = len(a)
a_max = n-1
a_min = 0
res = True
while res == True and a_min < n/2:
    if a[a_min] == a[a_max]:
        res = True
        a_max-= 1 
        a_min+= 1 
    else:
        res = False
if res == True:
    print ("yes")
else:
    print ("no")
