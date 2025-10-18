N = int(input('How many numbers you will enter : '))


sum = 0
c = 0



for i in range(1, N+1):
	x = int(input('Enter a value: '))
	if x > 6:
		sum = sum + x
		c = c + 1
avg = sum / c




print('sum =  ',sum)

print('Avarage = ' , avg)
