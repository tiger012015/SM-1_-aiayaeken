import random
import time

def OneDice(numbers):
    t1=time.clock()
    print("====================")
    print("One dice with 6 sides")
    print("numbers of run dice = ", numbers)

    sides = 6
    histogram = [0, 0, 0, 0, 0, 0]
    #This histogram count result of run dice 
    print(histogram)

    j = 0
    r = 0
    #Now,run the dice 
    while j < numbers :
        r = int(random.random()*sides) 
        histogram[r] = histogram[r] + 1
        j = j + 1
        
    #according to you required trials,the dice already run end
    
    print("s, N_s, N_s-N/6, N_s/N, N_s/N-1/6")
    j = 0
    while j < sides:
        print(j+1, histogram[j], histogram[j]-numbers/sides, histogram[j]/numbers, histogram[j]/numbers-1/6)
        j = j + 1

    t2=time.clock()
    print("run time =", t2-t1)


OneDice(1)
OneDice(10)
OneDice(100)
OneDice(1000)
OneDice(10000)
OneDice(100000)
OneDice(1000000)


