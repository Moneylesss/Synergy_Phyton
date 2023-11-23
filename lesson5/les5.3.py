mike = float(input())
ivan = float(input())
x_min = float(input())
if x_min <= mike and x_min <= ivan:
    print (2)
elif x_min <= mike:
    print ("Mike")
elif x_min <= ivan:
    print ("Ivan")
elif x_min <= (ivan+mike):
    print (1)
else:
    print (0)
