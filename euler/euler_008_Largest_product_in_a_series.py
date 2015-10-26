__author__ = "chlee"



if __name__:
	#try:
            n = """
               73167176531330624919225119674426574742355349194934
               96983520312774506326239578318016984801869478851843
               85861560789112949495459501737958331952853208805511
               12540698747158523863050715693290963295227443043557
               66896648950445244523161731856403098711121722383113
               62229893423380308135336276614282806444486645238749
               30358907296290491560440772390713810515859307960866
               70172427121883998797908792274921901699720888093776
               65727333001053367881220235421809751254540594752243
               52584907711670556013604839586446706324415722155397
               53697817977846174064955149290862569321978468622482
               83972241375657056057490261407972968652414535100474
               82166370484403199890008895243450658541227588666881
               16427171479924442928230863465674813919123162824586
               17866458359124566529476545682848912883142607690042
               24219022671055626321111109370544217506941658960408
               07198403850962455444362981230987879927244284909188
               84580156166097919133875499200524063689912560717606
               05886116467109405077541002256983155200055935729725
               71636269561882670428252483600823257530420752963450
               """
            a = int(raw_input())
            list = []
            max = 0
            temp = 0
            start_point = 0
            # phasing space
            for i in xrange(0, len(n)):
                if n[i] == " " or n[i] == "\n":
                    pass
                else:
                    list.append(int(n[i]))
            #print list
            #print len(list)
            
            for i in xrange(0, len(list)-a):
               for j in xrange(0,a):
                  if list[i+j] == 0:  # check if any element is zero
                      temp = 0
                  if list[i+j] == 1:  # check if any element is zero
                      temp = 0    
               
               for j in xrange(0,a):
               #   if list[i+j] == 0:  # check if any element is zero
               #       temp = 0
               #       break
               #   print "i,j : %d %d" %(i ,j)
                  temp += list[i+j]   # if no any element is zero, sum of group number
                  if j == 3:
                      if temp > max:
                        start_point = i
                        max = temp
                      temp = 0            
              # find out largest group number and remember start_point
                                                 
            print "max number = %d and start_point is %d" %( max,start_point )
            
              # now let's product the number
            temp = list[start_point]
            for i in xrange(1,a):
                print "temp, i : %d %d" %(temp,i)
                temp *= list[start_point+i]
                print temp
            print list[start_point:start_point+a]
            print "max product number is %d" %temp
            
            
            
            
	#except Exception,details:
     #       print details
