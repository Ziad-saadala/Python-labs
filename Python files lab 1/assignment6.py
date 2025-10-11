import math 
print("Calculate and print the number of days in N hours ")

print("please enter the number of hours ")
houres =int(input())

hourstodays = int((houres / 24 )) 
remain = int((houres % 24 ))

print("hourstodays = " , hourstodays , "day" , "and"  ,remain  , "hours" )
