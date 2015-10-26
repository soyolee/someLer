__author__ = "chlee"

from palindrome_number.module1 import palindrome
import timeit

start = timeit.default_timer()

#a = raw_input()
p = palindrome()
list = []
lagest = 0

for i in xrange(10000,1000,-1):
		for j in xrange(10000,1000,-1):
			x = i * j
			
			if lagest < x:
				pass
			else:
				continue	
			if p.findPalindrome(x):
					list.append(x)
					list.append(i)
					list.append(j)
					lagest = x
				#print "%s is palindrome" %i
			else:
				pass
		#print "can't find palindrome"
print "%s = %s * %s" %(list[-3],list[-2],list[-1])


stop = timeit.default_timer()

print "%.2f seconds" %(stop - start)