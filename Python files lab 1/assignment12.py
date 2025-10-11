import math


Units =  int(input("Please enter units: "))

Tens =  int(input("Please enter tens: "))

Hundreds =  int(input("Please enter hundreds: "))



# way 1 is put parts together  descending !not working if user put more than 1 digit !
print('The number is:',Hundreds,Tens,Units)    

# way 2 is addition 
print('The number is:',Hundreds* 100 +Tens *10 +Units *1)    