S1= input('Enter S1 : ')
S2= input('Enter S2: ')

for i in range  (len(S1)):
    if S1[i]!=   S2 [i]:
        print('mismatch at index' , i)

if S1 == S2 :
    print('Identical Strings')
