
import random
import time
import math


import tweepy
import getChatBotKeys
import matplotlib.pyplot as plt
import os

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
    myKeys = getChatBotKeys.GETTWITTER()
    CONSUMER_KEY = myKeys[0]
    CONSUMER_SECRET = myKeys[1]
    ACCESS_KEY = myKeys[2]
    ACCESS_SECRET = myKeys[3]
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    gcdTrue = 0
    gcdFalse = 0
    maxSize = 10000
    roll = 0
    st = time.time()
    piVals = []
    piTrials = []
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
	piVals.append(piEst)
	piTrials.append(gcdTrue+gcdFalse)
	if time.time() - st > 10*60:
	    print "Plotting"
	    st = time.time()
	    plt.plot(piTrials, piVals)
	    plt.axhline(y=math.pi, color='r', label="pi")
	    plt.ylabel('Pi Approximation')
	    plt.xlabel('Total Trials')
	    plt.title('Pi calculated from Two "Random Numbers" Coprime-ness')
	    plt.savefig("piAppx.png", bbox_inches='tight')
	    plt.close()
	    fn = os.path.abspath('piAppx.png')
	    msg = "Current #PiDay approximation of pi is " + str(piEst) + " after " + str(gcdTrue+gcdFalse) + " trials\nHappy Pi Day!"
	    print "Trying to Tweet"
	    try:
		api.update_with_media(fn, status=msg)
	    except TweepError:
		time.sleep(2)
		try:
		    api.update_with_media(fn, status=msg)
		except TweepError:
		    print "It's fucked man, two Tweep Errors in a row\n\tCheck what's up with twitter"

	    piVals = []
	    piTrials = []


    
main()











































