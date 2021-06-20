import random as r


def piCalc(n):
    count = 0
    for i in range (1,n+1):
        x = r.random()
        y = r.random()
        if (x*x + y*y) < 1:
            count +=1
        print(str(i) +" : "+ str(4*count/i))



piCalc(1000000)
