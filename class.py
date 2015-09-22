class Demo:
    def setAtt(self, a = 22, b = 33):
        self.a = a
        self.b = b
     
    def do_something(self):
        return self.a + self.b
 
print()
d = Demo()
d.setAtt()
print(d.do_something())
d.setAtt(11, 22)
print(d.do_something())
print()