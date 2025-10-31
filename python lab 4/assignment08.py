friends=input('enter friend list with (,) after every name : ').split(',')
presents=input('enter presents list with (,) after every present : ').split(',')
fav_pres=input('whats you wished to get? ')
if fav_pres in presents:
        for i in range(len(presents)):
   
            if presents[i] == fav_pres:
                print('Oh' ,friends [i+1], 'Thank you friend :) ')
                break
else:
    print('oops, Sorry none.')



