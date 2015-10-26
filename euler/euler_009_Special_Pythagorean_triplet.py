__author__ = "chlee"
import sys
import math

'''
#Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

try:
    if __name__ == "__main__":
        a = 1
        b = 1
        c = 1
        biggest = 0
        temp_a, temp_b, temp_c = 0, 0, 0
        # print math.pow(2, 2)
        while a + b + c <= 1000:
            print "a :", a
            a = a + 1
            for i in xrange(a, 1000):

                if biggest > (math.pow(a, 2) + math.pow(i, 2)):
                    pass
                else:
                    for j in xrange(a + b, 1000):
                        if a + i + j == 1000:
                            if math.pow(j, 2) > biggest:
                                if math.pow(a, 2) + math.pow(i, 2) == math.pow(j, 2):

                                    print "\t\t%s + %s = %s" % (a, i, j)
                                    print "\t\t\t%s + %s = %s" % (math.pow(a, 2), math.pow(i, 2), math.pow(j, 2))
                                    temp_a = a
                                    temp_b = i
                                    temp_c = j
                                    b = i
                                    c = j
                                    biggest = (math.pow(j, 2))

        print "%s + %s + %s = %s" % (temp_a, temp_b, temp_c, (temp_a + temp_b + temp_c))
        print "%s + %s = %s" % (math.pow(a, 2), math.pow(b, 2), math.pow(a + b, 2))
        print "biggest : %s" % biggest
        print "abc = %s" %(temp_a * temp_b * temp_c)
except Exception, details:
    print details
