x=input('write three names with semicolon(:) between them:-')
y=[i.strip() for i in x.split(':')]
for i,j in enumerate(y):
    print('Name'+str(i+1)+': ',j)

exit()
#with open('text.txt', 'r') as fl:
    #print(fl.read())
#towrite = ['First Line','Second Line','Third Line','Fourth Line','Fifth Line']
with open('text.txt', 'r') as fl:
    #print(type(fl.readlines()))
    lines=fl.readlines()
    print(lines)
    lines.pop(3)
    print(lines)

with open('text1.txt','w') as fl1:
    fl1.writelines(lines)
    #fl.write('\n')
    #fl.seek(2,1)
    #fl.writelines('\n'.join(i for i in towrite))
    #print([i+'\\f' for i in towrite])
    #print(fl.read(3))
    #print([next(fl) for x in towrite])

