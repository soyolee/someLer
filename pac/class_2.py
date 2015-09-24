__author__ = "chlee"

class bank:
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
	def deposit(self,amount):
		self.balance = amount + int(self.balance)
		return self.balance
	def withdraw(self,amount):
		self.balance = int(self.balance) - amount
		return self.balance
	def __str__(self):
		return 'bank({0}, {1})'.format(
            self.name, self.balance)