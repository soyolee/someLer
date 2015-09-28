__author__ = "chlee"

from e06_sum_squ.calc import calc

if __name__:
	p = calc()
	int(n) = raw_input()
	
	try:
		print p.sum_of_the_squares(n)
	except Exception,details:
		print details
	try:
		print p.square_of_the_sum(n)
	except Exception,details:
		print details
	try:
		print p.answer(n)
	except Exception,details:
		print details