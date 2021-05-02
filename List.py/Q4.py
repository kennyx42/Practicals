# Ask the user to enter a list containing numbers between 1 and 12. 
# Then replace all of the entries in the list that are greater than 10 with 10.
L=[]
for i in range (5):
    num=eval(input("Enter a list containing numbers between 1 and 12: "))
    L.append(num)
for x in range(len(L)):
    if L[x] > 10:
        L[x]=10
print(L)        

