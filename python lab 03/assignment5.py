value = int(input('Enter a value:'))
L = (input('Enter list of values:')).split()



c = 0

for i in L:
       if int(i) <= value:
    
         c = c + 1
    
                
                

print('=======================================')
print('your value is : ' , value )
print('your numbers are : ' , L )
print('=======================================')
if c == 0:
    print("ALL items are greater")
else:
    print(c, "numbers less than or equal to the given value")          
