import math 
print("Calculate and print the number of trays: ")

print("please enter the number of Cups ")
Cups =int(input())

print("please enter the max capacty of the tray")
MaxTray = int(input())

numOfTrays = math.ceil(Cups / MaxTray )

print("you will need  = " , numOfTrays  , "Tray")

