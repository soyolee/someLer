__author__ = "chlee"

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
	for i in range(100):
		if isPrime(i) == True:
			print i
			
#print(sum(i for i in range(10) if isPrime(i) == True ))

#print(sum(i for i in range(1000) if i%3 == 0 or i%5 == 0))