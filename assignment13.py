import random
num = random.randint(10,20)

print(" You have 5 chances to Gusse the Number from 10 : 20  ")




for i in range (5):
    User_Gusse= int(input ("Gusse the Number from 10 : 20 "))
    if User_Gusse == num :
        print ("Well Done! You got it right  ")
        break              # stop the loop here // search done 

    else : 
        print("wrong try Again!")