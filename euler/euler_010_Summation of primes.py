__author__ = "chlee"
import sys
import math
# find prime number

from findPrime.prime import prime

if __name__ == "__main__":

    sum = 0
    # step one : find out sqrt of user input number
    primelist = []
    input001 = int(raw_input())


    # step two : find out prime number
    p = prime()
    for i in range(input001):
        if p.findPrime(i) == True:
            #print i
            primelist.append(i)
            sum = sum + i
print primelist
print "sum : %s" %sum

    # step three : div input001 from prime

for j in primelist:
    if (input001 % j) == 0:
        print j

