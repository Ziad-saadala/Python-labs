#2
'''
assignment =input('enter yes or no')

price = float(input(' enter price'))

if assignment.lower() == 'yes':
    if price > 900:
        print(' dad will pay')
    else:
        print('mom will pay')

else : 
    print('no shoes')

    '''


#3 
'''
inlist = input('enter your items').split()

for x in 'battery' :
     0==0

if x in inlist:
     print('you dont need a bettery')
else :
     print('you will need to buy a battery')'''
#4,,,
'''
n1= int(input('enter number  : '))
n2=int(input('enter num 2: '))
n3=int(input('enter num 3: '))
list =[n1,n2,n3]

list.sort()

print(list),,,'''

#5
'''
weg = int(input(' enter weight: '))

if weg >0 :
    click=int(input('1 from millgram to gram , 2 from Kg to gram , 3 from ton to gram'))
    if click == 1:
        print(weg /1000 , 'grams')

    elif click ==2:
        print(weg * 1000 , "grams")

    elif click ==3 :
        print(weg * 1000000 , "grams")

else:
    print('weight cant be negative or 0')

    '''

#6
vig = ['vegetables',  'mushroom' ,'mashed potatoes']
ham = ['burger', 'grilled chicken','seafood']


print(vig)
print(ham)



x = input('chose first option')
y = input('chose second option')
if x in vig and y in vig:
    print(' you love vigitables')
elif x in ham and y in ham :
    print(' u like meat alot')

else :
    print(' you are balanced person')