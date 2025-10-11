import math

print("Celsius units (Tc), calculate the corresponding values of Kelvin units Tk")   
        


Celsius =  float(input("enter Celsius  "))
#=====================================تحويلات ===========================================================

#Tc = Tf * 5/9 - 32 
#Tk = Tr * 5/9
#Tr =Tf + 459.67
#Tf = 5/9 Tc + 32 
# so Tk = 5/9* (9/5 * Celsius + 32 + 459.67)


#==================================================================================================

Tk = float( 5/9* (9/5 * Celsius + 32 + 459.67))
print(Tk , 'Kelvin')    
