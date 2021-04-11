from random import choice
score=0
score1=0
for x in range (1,6):
    namelist=['Rock','Paper','Scissor']
    z=choice(namelist)
    y=input('Enter either Rock, Paper or Scissor')
    if(y=='Rock' and z=='Rock'):
        if('Draw'):
            print(x,score=score+0,'and',score1=score1+0)
    if(y=='Rock' and z=='Paper'):
        print(x,'Player 1 - Computer 0')
    if(y=='Rock' and z=='Scissor'): 
        print(x,'Player 1 - Computer 0')
    if(y=='Paper' and z=='Paper'):
        print(x,'Draw')    
    if(y=='Paper' and z=='Rock'):  
        print(x,'Player 0 - Computer 1')   
    if(y=='Paper' and z=='Scissor'):
        print(x,'Player 0 - Computer 1')  
    if(y=='Scissor' and z=='Scissor'): 
        print(x,'Draw') 
    if(y=='Scissor' and z=='Rock'):   
        print(x,'Player 0 - Computer 1')  
    if(y=='Scissor' and z=='Paper'):  
        print(x,'Player 1 - Computer 0')  
    


    





