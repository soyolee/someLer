__author__ = "chlee"
import sys
import math
# find prime number

def isPrime(n):  
    if n <= 1:  
        return False 
    i = 2 
    while i*i <= n:  
        if n % i == 0:
            #print "enter while %s" %i
			return False 
        i = i + 1
    return True 
	
if __name__ == "__main__":

    # step one : find out sqrt of user input number
    prime = []
    input001 = int(raw_input())
    step1_number = int(math.sqrt(input001))
    print "sqrt : " + str(step1_number)

    # step two : find out prime number

    for i in range(step1_number):
        if isPrime(i) == True:
            #print i
            prime.append(i)

print prime

    # step three : div 


#print(sum(i for i in range(10) if isPrime(i) == True ))

#print(sum(i for i in range(1000) if i%3 == 0 or i%5 == 0))