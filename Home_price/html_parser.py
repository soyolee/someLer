__author__ = 'chlee'

import urllib2
import string
import re
import datetime


date = datetime.datetime.now()

zillow_say = "This report generate on %s-%s-%s \n\nHow often are Zestimates for homes updated ? \n We refresh Zestimates for all homes three times a week. On rare occasions, this schedule is interrupted by operations associated with algorithmic changes or the deployment of new analytic features" %(date.year,date.month,date.day)

list = (
   "http://www.zillow.com/san-jose-ca/home-values/",
   "http://www.zillow.com/north-san-jose-san-jose-ca/home-values/",
   "http://www.zillow.com/santa-clara-ca/home-values/",
   "http://www.zillow.com/sunnyvale-ca/home-values/",
   "http://www.zillow.com/cupertino-ca/home-values/",
   "http://www.zillow.com/mountain-view-ca/home-values/",
   "http://www.zillow.com/los-altos-ca/home-values/",
   "http://www.zillow.com/palo-alto-ca/home-values/",
   "http://www.zillow.com/menlo-park-ca/home-values/",
   "http://www.zillow.com/foster-city-ca/home-values/",
   "http://www.zillow.com/redwood-city-ca/home-values/",
   "http://www.zillow.com/san-mateo-ca/home-values/",
   "http://www.zillow.com/south-san-francisco-ca/home-values/",
   "http://www.zillow.com/san-francisco-ca/home-values/",
   "http://www.zillow.com/milpitas-ca/home-values/",
   "http://www.zillow.com/fremont-ca/home-values/",
   "http://www.zillow.com/newark-ca/home-values/",
   "http://www.zillow.com/union-city-ca/home-values/",
   "http://www.zillow.com/hayward-ca/home-values/",
   "http://www.zillow.com/pleasanton-ca/home-values/",
   "http://www.zillow.com/san-ramon-ca/home-values/",
   "http://www.zillow.com/dublin-ca/home-values/",
   "http://www.zillow.com/livermore-ca/home-values/"
   "http://www.zillow.com/san-ramon-ca/home-values/",
   "http://www.zillow.com/reno-nv/home-values/",
   "https://www.zillow.com/campbell-ca/home-values/"
   
)
print "******************"
print zillow_say
print "******************\n"

for pointer in list:
    content = urllib2.urlopen(pointer).read()
    content = content.split("\n")

    for i in content:
        # if "Zillow Home Value Index" in i :
        if "is $" in i:
            j = re.findall(r"[\w']+", i)
            city = str(j[0:j.index("is")]).translate(None, "'")
            city = city.translate(None, ",")
            city = city.translate(None, "]")
            city = city.translate(None, "[")
            price = str(j[j.index("is")+1:]).translate(None, "'")
            price = price.translate(None, "[")
            price = price.translate(None, "]")
            price = price.translate(None, " ")
            #print " %s\t\t\t\t %s\t$ %s" %(city,j[j.index("is")],price)
            print '{0:30s} is\t $ {1}'.format(city, price)
	    break
