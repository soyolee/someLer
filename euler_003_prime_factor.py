__author__ = "chlee"
import sys
import math
# find prime number

from findPrime.prime import prime

if __name__ == "__main__":

    # step one : find out sqrt of user input number
    primelist = []
    input001 = int(raw_input())
    step1_number = int(math.sqrt(input001))
    print "sqrt : " + str(step1_number)

    # step two : find out prime number
    p = prime()
    for i in range(step1_number):
        if p.findPrime(i) == True:
            #print i
            primelist.append(i)
			
print primelist

    # step three : div input001 from prime
	
for j in primelist:
	if (input001 % j) == 0:
		print j
	
	