""""
s=input('Enter a Text:')
print('(a)',len(s))
print('(b)',s*10)
print('(c)', s[0])
print('(d)', s[:3])
print('(e)', s[-3:])
print('(f)', s[::-1])
if len(s)>7:
	print('(g)',s[6])
print('(h)', s[1:-1])	
print('(i)', s.upper())
print('(j)', s.replace('a','e'))
if s.isalpha():
	print('(k)', s.replace(s[:],''))
	"""
"""
s=('You want to go or you want to stay')
b=s.count('')
a=s.count(' ')
print(b-a)
"""
"""
s=input('Enter a Formular:')
a=s.count('(')== s.count(')')
if a:
    print('we have the same number of parenthesis')
else:
    print('Please recheck your Formula')
"""
"""
s='aeiou'
p=input('Enter a Text:')
for i in range (len(s)):
    if s[i] in p:
    	print(s[i])
"""
"""
s=input('Enter a Text:')	
new_string=s[:1]+'*'+s[2:]+'!!!'
print(new_string)	
"""
new=''
other=''
s='arise and shine'
for i in range(len(s)):
	if s[i]!=(' '):
		print(s[i], end='')





	


    			
