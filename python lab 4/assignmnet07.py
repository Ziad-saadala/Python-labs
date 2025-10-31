#program that reads the coefficients (a, b, c) of the quadratic
# equation ax2 +bx + c = 0. The program computes the roots (x1 and x2) if they exist
import math
print('This program calculate quadratic equation ax2 + bx + c = 0 ')

a = float(input('pls enter a '))
b = float(input('pls enter b '))
c = float(input('pls enter c '))

# any x is a solution (if a = b = c = 0)
if a == b == c ==0:
    print('any x is a solution')
#no solution (if a = b = 0, c ~= 0)
elif a == b == 0 and c != 0 :
    print('no solution')

#one real root (if a = 0, so the root is −c/b)
elif a == 0:
    print('the root is : ' , -c/b)
#two real or complex roots (if not any of the above cases)
else:
    root1= (-b+math.sqrt(b**2-4*a*c))/(2*a)
    root2= (-b-math.sqrt(b**2-4*a*c))/(2*a)
    print('root 1 : ' , root1)
    print('root 2 : ' , root2)
