import math

print('Display N grams in the form of number of kilograms and number of grams.')   


print('Enter Your number of grams')   
grams =  int(input())


#فاصل
print('=======================================================================================')   



Kilogram = int(grams/1000)

part_grams = int(grams % 1000)

 
print(Kilogram  , "Kilo Gram")    
print(part_grams,    "Gram")    