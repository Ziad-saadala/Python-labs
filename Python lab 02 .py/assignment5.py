"""for i in range(start, end, step):
    print(i)
"""
# start = 1, end = 9, step = 2      Output =  (1 -3-5-7)
# start = 9, end = 1, step = 2      Output =  (there will be not because start couldnt reach end its more bigger)
# start = 9, end = 1, step = -2     Output =  (step is negative so start will decrease to match the end and output is 9-7-5-3)
# start = 1, end = 9, step =  0     Output =  (Error step must be possative or negative 0 is not logical to start a loop)