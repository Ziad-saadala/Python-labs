Students_Grades = input('Enter student grades').split()

print("====================check if grades is in range=============================")
#A check if grade between range (0-100)
for i in Students_Grades : 
    if int(i) >100 or int(i) <0  :
        print('invalid Grade [0>grade>100]')
print("========================Produce a corresponding list======================================")

#B a corresponding list (0-1)
corres = []
for i in Students_Grades : 
    if int(i) >100 or int(i) <0  :
        corres.append(0)
    else:
        corres.append(1)
print(corres)
print("====================get sum then calc avrage=============================================")



#C get sum and number of valid grades then calc avrage
sum =0
c=0
for i in Students_Grades : 
    if int(i) <100 or int(i) >0  :
       sum = int(i)+sum
       c=c+1

Avrage = sum /c
print("number of students = ",c)
print('Avrage of students grades is = :  ',Avrage)


print("=====================Find and display the highest and lowest==grades==========================================")


#D Find and display the highest and lowest grades and specify their locations.

highest =  int(Students_Grades[0])
lowest = int( Students_Grades[0])


for i in range (len(Students_Grades)) :

        if int(Students_Grades[i]) >=highest  :
                highest = int(Students_Grades[i])
                high_index = i
                
        if int(Students_Grades[i]) <=lowest   :
                lowest = int(Students_Grades[i])
                low_index = i


print('highest student have  = : ' , highest ,'at ' ,high_index)
print('lowest student have  =: ' ,lowest, 'at' , low_index)


print("============student + 85%===================================================")

#E student + 85%
Student_85=0
for i in range (len(Students_Grades)) :

        if int(Students_Grades[i]) >85  :
           Student_85= Student_85+1

print(Student_85 ,'Student have more than 85% ')

print("================= students having grades greater than average============================================")

#F  Locate and display students having grades greater than average, and display their count.


Above_avg = int(Students_Grades[0])
Above_avg_count = 0


for i in range (len(Students_Grades)) :

        if int(Students_Grades[i]) >Avrage  :
                Above_avg = int(Students_Grades[i])
                Above_index = i
                Above_avg_count = Above_avg_count + 1
                
       

print( ' Student Above Avrage has ', Above_avg,'point'  ,'at ' ,Above_index)
print('count of Students above avrage =: ' ,Above_avg_count, "Student")

print("=====================================================================")
print("=====================================================================")
print("=====================================================================")
print("=====================================================================")
