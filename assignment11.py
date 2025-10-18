import math 
print("Write a program that gets two positive integer numbers X and Y and calculates")

Base = int(input("Enter Base "))

Power = int(input("Enter Power "))

R = 1
for i in range (1 , Power+1):           # Start looping Power time and multply Base * Base depend on Power value
    R = R * Base

print(R)








'''
#Method 2 
X = int(input("Enter first Number the Base"))
Y = int(input("Enter Second Number the Power"))

Result = X ** Y

print("Result = " ,  Result)'''