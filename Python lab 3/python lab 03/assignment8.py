Userinput= input('Enter your numbers: ')
squarelist=[]
for i in Userinput.split():
    x = int(i)**2
    squarelist.append(x)

print('=======================')
print('A = ' , Userinput)
print('B = ', squarelist)
print('=======================')