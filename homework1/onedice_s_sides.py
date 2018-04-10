import random
import time

def OneDiceS(numbers, sides):
    t1=time.clock()
    print("====================")
    print("Number of sides = ", sides)
    print("Number of roll dice = ", numbers)

    histogram = []
    for s in range(sides):
        histogram.append(0)
    print(histogram)

    r = 0
    for t in range(numbers):
        #anyone parameter ,it only use in roll dice
        r = int(random.random()*sides)
        histogram[r] = histogram[r] + 1
    print( histogram)
    #theoretical prediction
    mean = 0
    meansq = 0
    for k in range(sides):
        mean = (k+1) * 1/sides + mean
        meansq = (k+1) **2 * 1/sides + meansq
        
        
    variance = meansq - mean ** 2
    standard = variance ** 0.5
           
    print("s, N_s, N_s-N/sides, N_s/N, N_s/N-1/sides")
    
    sum = 0
    sumsq = 0
    for s in range(sides):
        print(s+1, histogram[s], histogram[s]-numbers/sides, histogram[s]/numbers, histogram[s]/numbers-1/sides)
        one = (s+1)* histogram[s]
        sum = one + sum
        onesq = (s+1) ** 2 * histogram[s]
        sumsq = onesq + sumsq
    exmean = sum/numbers
    exvariance = sumsq/numbers-exmean*exmean
    exstandard = exvariance**0.5
    print("Theoretically ","mean =", mean, "variance =", variance, "standard =",standard )  
    print("Experimentally " , "mean =", exmean, "variance =", exvariance, "standard =",exstandard )
    print("experimental error :","mean error = ",abs(1-exmean/mean)*100,"%" ,"standard error = ",abs(1-exstandard/standard)*100,"%")
    t2=time.clock()
    print("run time =", t2-t1)


OneDiceS(1, 6)
OneDiceS(10, 6)
OneDiceS(50, 6)
OneDiceS(100, 6)
OneDiceS(1000, 6)
OneDiceS(10000, 6)
OneDiceS(100000, 6)
OneDiceS(1000000, 6)


