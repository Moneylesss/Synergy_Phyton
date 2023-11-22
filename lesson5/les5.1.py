a = int(input())
if (a < 0) and ((a % 2) == 0):
    print ("otricatelnoe chetnoe chislo")
elif (a < 0) and ((a % 2) == 1):
    print ("otricatelnoe nechetnoe chislo")
elif (a > 0) and ((a % 2) == 0):
    print ("polozhitelnoe chetnoe chislo")
elif (a > 0) and ((a % 2) == 1):
    print ("polozhitelnoe nechetnoe chislo")
else: 
    print ("nylevoe chislo")
