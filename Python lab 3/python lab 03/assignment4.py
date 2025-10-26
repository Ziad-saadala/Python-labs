L = input('Enter list of values:').split()
for i in range (len(L)):
    if int(L[i]) > 0:

        print(L[i])


#4 method 2  by  value

L = input('Enter list of values:').split()
for i in L:
    if int(i) > 0:
         print(i)

