__author__ = "chlee"

class palindrome:
	
	def __init__(self):
		pass
	def findPalindrome(self,n):
		self.n = n
		b = str(self.n)
		a_list = []
		for i in b:
			a_list.append(i)

		if a_list == list(reversed(a_list)):
			return True
		else:
			return False