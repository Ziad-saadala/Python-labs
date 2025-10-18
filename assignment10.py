import math     
print ('Enter how many numbers you will enter')

N= int(input())
Sum_Even =0
Sum_ODD  =0

for i in range (1 , N+1):

    x = int(input('Enter a value: '))

    if x % 2 == 0  : 
        Sum_Even = Sum_Even + x

    else :
        Sum_ODD = Sum_ODD + x 








print ('==================bariar=================' )
print ('==================bariar=================' )
print ('==================bariar=================' )


print ('Even =  ' , Sum_Even)
print ('==================bariar=================' )
print ('ODD  =  ' , Sum_ODD)




