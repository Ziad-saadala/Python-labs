import math     
print ('Enter a Possative number   prints the sum of the series: Sum = 1^2 + 2^2 + 3^2 + 4^2 + . . . N^2 ')
N=int(input())

sum = 0
if N > 0 : 
   
    for i in range (1 , + N+1):
        sum = sum + i **2

else :
    print('Invalid Negative number or 0')


print('Sum = ',sum)
