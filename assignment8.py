print('a program that reads two integer values N1 and N2 and calculates and prints the summation of numbers between N1 and N2 and their average.')
Numb1 = int(input('Enter number 1 '))
Numb2 = int(input('Enter number 2 '))

sum =0 
c=0
for i in range (Numb1 , Numb2 +1 ):

    sum = sum + i   
    c=c+1
print('sum = ', sum)
print('Avarage = ', sum / c)