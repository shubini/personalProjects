#this was the first function to tackle the problem of calculating pi with one random number generaotr I created. This function takes a single parameter n, which is the number of trials that the monte carlo sim goes through.
import random as r

# The principle of this function essentially relies on a co-ordinate system. Imagine a circle of radius r inside a square of length 2r plotted onto an xy axis with the centre of both the square and the circle on the origin.
#If we were to plot random points, the fraction of random samples that would be inside the is pi / 4.
#The proportion is the same for all 4 quarters, so we can just use the positive quadrant to simplifiy the problem 
#Once we have our set of samples, the fraction inside the circle * 4 is our estimate for pi



def piCalc(n):
    count = 0 #count measures the amount of samples inside the circle
    for i in range (1,n+1): #occures n times for the n samples
        x = r.random() #samples an x coordinate
        y = r.random() #samples a y coordinate
        if (x*x + y*y) <= 1: #given that the circle has radius 1, if y^2+x^2 is less than or equal to 1, it lies on the circle, otherwise its outside
            count +=1 #if its inside the circle, add 1 to count
    piEstimate = 4*count/n # estimate pi -  count/n = pi/4, so pi = 4* count/n
    return(piEstimate) # return estimate



print(piCalc(1000000)) #show the estimate after 1M samples
