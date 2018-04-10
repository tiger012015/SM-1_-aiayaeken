# Assignment 1
### student id : 106022556

### Problem 0: One die with 6 sides

**Some of My data**

One dice with 6 sides
> numbers of run dice =  1 
>>s, N_s, N_s-N/6, N_s/N, N_s/N-1/6  
1 0 -0.16666666666666666 0.0 -0.16666666666666666  
2 0 -0.16666666666666666 0.0 -0.16666666666666666  
3 0 -0.16666666666666666 0.0 -0.16666666666666666  
4 0 -0.16666666666666666 0.0 -0.16666666666666666  
5 1 0.8333333333333334 1.0 0.8333333333333334  
6 0 -0.16666666666666666 0.0 -0.16666666666666666  
run time = 0.00046528813618351705  

> numbers of run dice =  1000  
>>s, N_s, N_s-N/6, N_s/N, N_s/N-1/6  
1 182 15.333333333333343 0.182 0.015333333333333338  
2 162 -4.666666666666657 0.162 -0.004666666666666652  
3 190 23.333333333333343 0.19 0.023333333333333345  
4 173 6.333333333333343 0.173 0.00633333333333333  
5 135 -31.666666666666657 0.135 -0.03166666666666665  
6 158 -8.666666666666657 0.158 -0.008666666666666656  
run time = 0.0011238761253480334  

 
>numbers of run dice =  1000000  
>>s, N_s, N_s-N/6, N_s/N, N_s/N-1/6  
1 166372 -294.66666666665697 0.166372 -0.0002946666666666653  
2 166272 -394.66666666665697 0.166272 -0.0003946666666666543  
3 166573 -93.66666666665697 0.166573 -9.366666666665857e-05  
4 166413 -253.66666666665697 0.166413 -0.00025366666666665205  
5 167048 381.33333333334303 0.167048 0.0003813333333333446  
6 167322 655.333333333343 0.167322 0.0006553333333333411  
run time = 0.535182283470931

**Question 4:As the number of trials increases, does the magnitude (absolute value) of the differences between the number of times a given side occurs and one-sixth of the number of trials increase or decrease?**  

According to my data, i think this answer is decrease,see 1000000 number of run dice, this order of value is close to 1*e-04, very small.

**Question 5:As you increase the number of trials, does the ratio of the number of times each side occurs to the total number of trials approach closer to 1/6?**

See 1000000 number of run dice, 1/6 is close to 0.166666666, this value quite match my data.


### Problem 1: One die with S sides

**Question 3:Run your program for two different values of S. Are the results for the mean, variance, and standard deviation consistent with your predictions?**

If S=6, theoretically mean=3.5 variance=2.91666666667 standard=1.707825
If S=10  mean = 5.5 variance = 8.25 standard = 2.8722813232690143

**Capture from my data**

> Number of sides =  6  
>>Number of roll dice =  1  
[0, 0, 0, 0, 0, 0]  
[0, 0, 0, 0, 1, 0]  
Theoretically  mean = 3.5 variance = 2.916666666666668 standard = 1.7078251276599334  
Experimentally  mean = 5.0 variance = 0.0 standard = 0.0  
experimental error : mean error =  42.85714285714286 %     standard error =  100.0 %  
run time = 0.0012681382504524663  

>Number of sides =  6  
>>Number of roll dice =  50  
[0, 0, 0, 0, 0, 0]  
[6, 15, 4, 11, 9, 5]  
Theoretically  mean = 3.5 variance = 2.916666666666668 standard = 1.7078251276599334  
Experimentally  mean = 3.34 variance = 2.5044000000000004 standard = 1.5825296205758679  
experimental error : mean error =  4.571428571428571 %     standard error =  7.336553670207779 %  
run time = 0.0016296488902298734  

>Number of sides =  6  
>>Number of roll dice =  1500  
[0, 0, 0, 0, 0, 0]  
[262, 237, 254, 258, 261, 228]  
Theoretically  mean = 3.5 variance = 2.916666666666668 standard = 1.7078251276599334  
Experimentally  mean = 3.4686666666666666 variance = 2.873018222222223 standard = 1.694998000654344  
experimental error : mean error =  0.8952380952380934 %     standard error =  0.75107965082849 %  
run time = 0.0017710599859128706  

====================  
>Number of sides =  10  
>>Number of roll dice =  1  
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
[0, 0, 0, 1, 0, 0, 0, 0, 0, 0]  
Theoretically  mean = 5.5 variance = 8.25 standard = 2.8722813232690143  
Experimentally  mean = 4.0 variance = 0.0 standard = 0.0  
experimental error : mean error =  27.27272727272727 %     standard error =  100.0 %  
run time = 0.00205217157053994  

>Number of sides =  10  
>>Number of roll dice =  50  
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
[6, 5, 8, 8, 4, 4, 5, 1, 5, 4]  
Theoretically  mean = 5.5 variance = 8.25 standard = 2.8722813232690143  
Experimentally  mean = 4.88 variance = 7.865600000000001 standard = 2.804567702873297  
experimental error : mean error =  11.272727272727279 %     standard error =  2.3574856629520857 %  
run time = 0.0015452583975275047  

>Number of sides =  10  
>>Number of roll dice =  10000  
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  
[1001, 946, 1021, 972, 970, 1023, 986, 1023, 1036, 1022]  
Theoretically  mean = 5.5 variance = 8.25 standard = 2.8722813232690143  
Experimentally  mean = 5.5462 variance = 8.290265560000005 standard = 2.8792821258084462  
experimental error : mean error =  0.8399999999999963 %     standard error =  0.2437366591746093 %  
run time = 0.005222517211223021  

According to my data, mean variance, and standard deviation consistent with my theoretical prediction

**Question 4:Experiment with different numbers of trials. How many trials do you need to obtain a rough estimate for the values of the mean and standard deviation? How many trials do you need to obtain an error of less than 1%? Do you need the same number of trials to obtain 1% accuracy for the mean and standard deviation.**

I think 1000 trials can provide a rough value, but more and more accurate.

If we want to error less than 1% , trials greater than 1500.

This is random, so 1000 trials or 800 trials may also obtain 1% accuracy for the mean and standard deviation.
But more trials can precise obtain an error of less than 1%,let us get more close to theoretical data.
