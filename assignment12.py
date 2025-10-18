print("displays the trip time.")

Start = float(input("Enter Departure Time in (X.yy format)"))

End = float(input("Enter Arrival Time in (X.yy format)"))


Start_Hours = int(Start)
Start_Minuets = float(Start) - int (Start)

End_Hours = int(End)
End_Minuets = float(End) - int (End)

Trip_time = ((End_Hours *60 )+(End_Minuets *100)) - ((Start_Hours* 60 ) + (Start_Minuets *100)) 

Trip_Houers = int(Trip_time // 60) 
Trip_Minutes = int(Trip_time % 60)

print ("Trip time will take" , Trip_Houers , "Houres  " , "and ", Trip_Minutes ,  "Minutes ")