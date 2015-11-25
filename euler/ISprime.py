__author__ = "chlee"
import sys
import math
import timeit

# find prime number

from findPrime.prime import prime

if __name__ == "__main__":
    
    start = timeit.default_timer()
    # step one : find out sqrt of user input number
    primelist = []
    
    i = 1
    stack = 0
    p = prime()
    print "\n\nNow in progress:\n"
    while True:
        if p.findPrime(i) == True:

            if p.findPrime(2*i + 1 ) == True:
                primelist.append(i)            
                if len(primelist) % 1000 == 0:
                    stack += 1000
                    del primelist[0:1000]
                    stop = timeit.default_timer()
                    print "\r"*60,               
                    print "\t"+str(stack),
                    #print "\t"+str(len(primelist)),
                    print "\t\t Run time : %.2f seconds" %(float(stop - start)), 
        
        if (stack + len(primelist)) == 200702:
            print "\n"+"*"*60+"\n"
            print primelist
            break
            
        i += 1