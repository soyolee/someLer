class prime:
	def __init__(self):
		pass
		
	def findPrime(self,n):
		if n <= 1:  
			return False 
		i = 2 
		while i*i <= n:  
			if n % i == 0:
				#print "enter while %s" %i
				return False 
			i = i + 1
		return True 