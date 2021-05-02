# Write a program that generates a list of 20 random numbers between 1 and 100
#2(a):Print the list
from random import randint
L=[]
for i in range (20):
    L.append(randint(1,100))
print(L)

#2(b): Print the average of the elements in the list
average_element=sum(L)/len(L)
print(average_element)

#2(c):Print the largest and smallest values in the list
largest_value= max(L)
smallest_value=min(L)
print(largest_value,',' ,smallest_value)

#2(d):Print the second largest and second smallest entries in the list
L.sort()
print(L)
print('Second largest',L[-2], 'and','Second smallest', L[1])

#2(e):Print how many even numbers are in the list
NewList=[]
for item in L:
    if item%2==0:
        NewList.append(item)
print(len(NewList)) 

       

        
