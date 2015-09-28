__author__ = "chlee"

import math

class calc:
	def __init__(self):
		pass
	def sum_of_the_squares(self,n):
		sum = 0
		for i in xrange(1,n+1):
			sum += math.pow(i,2) 
		return sum
	def square_of_the_sum(self,n):
		return math.pow(((1+n)*n)/2,2)
	def answer(self,n):
		return self.square_of_the_sum(n) - self.sum_of_the_squares(n)