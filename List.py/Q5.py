#Ask the user to enter a list of strings.
#Create a new list that consists of those strings with their first characters removed      
newstring_list=[]
for i in range (4):
    oldstring=input('Enter any word: ')
    oldstring=oldstring[1:]
    newstring_list.append(oldstring)
print(newstring_list)

