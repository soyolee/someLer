__author__ = "chlee"
import sys
import math
# find prime number

from findPrime.prime import prime

try:

    if __name__ == "__main__":


    # step one : find out sqrt of user input number
        primelist = []
        input001 = int(raw_input())
        #input001 = int(input001)
    #step1_number = int(math.sqrt(input001))
    #print "sqrt : " + str(step1_number)

    # step two : find out prime number
        p = prime()
        i = 1
        
        while len(primelist) < input001:
            #print i
            if p.findPrime(i) == True:
               #print i
               primelist.append(i)
               #print "length of primelist is %d" %len(primelist)
               #print ''
            i += 1
        print primelist[-1]

except Exception,details:
		print details    
    
    # step three : div input001 from prime

'''	
for j in primelist:
	if (input001 % j) == 0:
		print j
'''
	