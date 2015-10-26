__author__ = "chlee"


a = 1
divable = 0		# divable = 1 means this number is not the multiple number
find = 0 		# find equal to 1 means find out the number

while find == 0:
	for i in xrange(20,0,-1):
		#print i

		if int(a) % i == 0:
			pass
		else:
			divable = 1
			break
	if divable == 0 :
		print "%s is multiple number" %str(a)
		find = 1
	else:
		#print "%s is not multiple number" %str(a)
		divable = 0
		a += 1
		
