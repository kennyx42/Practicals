# Start with the list [8,9,10]. Do the following:
# 3(a): Set the second entry (index 1) to 17
L=[8,9,10]
L.insert(1,17)
print(L)

#3(b):  Add 4, 5, and 6 to the end of the list
new=[4,5,6]
for i in new:
    L.append(i)
print(L)

#3(c):Remove the first entry from the list
L.pop(0)
print(L)

#3(d):Sort the list
L.sort()
print(L)

#3(e): Double the list
L=L*2
print(L)


#3(f):Insert 25 at index 3
L.insert(3,25)
print(L)

