word = input()
a = "a"
a_count = word.count(a)
e = "e"
e_count = word.count(e)
i = "i"
i_count = word.count(i)
o = "o"
o_count = word.count(o)
u = "u"
u_count = word.count(u)
y = "y"
y_count = word.count(y)
vow = a_count + e_count + i_count + o_count + u_count + y_count
if a_count == 0:
    a_count = "False"
if e_count == 0:
    e_count = "False"
if i_count == 0:
    i_count = "False"
if o_count == 0:
    o_count = "False"
if u_count == 0:
    u_count = "False"
if y_count == 0:
    y_count = "False"
print ("Kolicestvo glasnyh:",vow)
print ("a:", a_count)
print ("e:", e_count)
print ("i:", i_count)
print ("o:", o_count)
print ("u:", u_count)
print ("y:", y_count)
