Userinput= input('Enter your statment: ')
#vowels=['a' 'i' 'e' 'u' 'o' ]
c=0
for v in range (len(Userinput)):
    if (Userinput[v] == 'a' or Userinput[v] == 'A' or
        Userinput[v] == 'e' or Userinput[v] == 'E' or
        Userinput[v] == 'i' or Userinput[v] == 'I' or
        Userinput[v] == 'o' or Userinput[v] == 'O' or
        Userinput[v] == 'u' or Userinput[v] == 'U'):
            
            c = c+1


print('you have ',c , 'vowels in your statment')