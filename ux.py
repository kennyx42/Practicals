s=('I can\'t allow :this to append""')
s=s.lower()
for i in ':\'"':
    s=s.replace(i,'')
print(s)

    