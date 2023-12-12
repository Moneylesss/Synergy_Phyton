f = list(map(int, input().split()))
m = set()
n = len(f)
for i in range (n):
    if f[i] in m:
        print (f[i], "- Yes")
    else:
        m.add(f[i])
        print (f[i], "- NO")
