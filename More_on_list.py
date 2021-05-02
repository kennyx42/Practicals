from random import shuffle
name=['Jane','sue','billie','overt']
shuffle(name)
teams=[]
for i in range(0,len(name),2):
    teams.append([name[i], name[i+1]])
print(teams)    