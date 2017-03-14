
import random
import time
import math

# Idea Thanks to the wonderful Matt Parker
#   https://www.youtube.com/watch?v=RZBhSi_PwHU



def gcd(x, y):
    gcd = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd




def main():
    gcdTrue = 0
    gcdFalse = 0
    maxSize = 10000
    roll = 0
    while True:
	for i in range(1000):
	    a = int(random.random()*maxSize + 1)
	    b = int(random.random()*maxSize + 1)
	    abGCD = gcd(a,b)
	    if abGCD > 1:
		gcdTrue += 1
	    else:
		gcdFalse += 1
	    #roll += 1
	time.sleep(0.00001)
	#print gcdTrue, gcdFalse
	pOfGCDFalse = float(gcdFalse)/float(gcdTrue+gcdFalse)
	#print pOfGCDFalse
	piEst = math.sqrt(6./pOfGCDFalse)
	print math.pi
	print piEst
	print ""

    
main()
