L=[2,4,11,12,4,5,1,76,99,5,3]
count=0
# 1(a): Print the total number of items in the list
number_of_items=len(L)
print(number_of_items)

# 1(b): Print the last item in the list.
print (L[-1])

# 1(c): Print the list in reverse order
L.reverse()
print(L)

# 1(d): Print Yes if the list contains a 5 and No otherwise
if 5 in L:
    print('Yes')
else:
    print('No')

# 1(e): Print the number of fives in the list
number_of_fives =L.count(5)
print(number_of_fives)

# 1(f):Remove the first and last items from the list, sort the remaining items, and print the result
print(L)
del L[0]
del L[-1]
print(L)

# 1(g):Print how many integers in the list are less than 5
list_less_than_5=[]
for item in L:
    if item <5:
       list_less_than_5.append(item)
print(len(list_less_than_5))     