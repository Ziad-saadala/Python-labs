
F = 'y'  
while F == 'y':
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
            print('Invalid Unit')

    else:
        print('weight cant be negative or 0')

    F = input('do you want to continue (y/n)?')
else: 
    print('GoodBye <3...')