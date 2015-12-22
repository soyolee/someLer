"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt
import urllib2
import string
import re
import datetime

date = datetime.datetime.now()


zillow_say = "This report generate on %s-%s-%s \n\nHow often are Zestimates for homes updated ? \n We refresh Zestimates for all homes three times a week. On rare occasions, this schedule is interrupted by operations associated with algorithmic changes or the deployment of new analytic features" %(date.year,date.month,date.day)

list = (
   "http://www.zillow.com/san-jose-ca/home-values/",
   "http://www.zillow.com/santa-clara-ca/home-values/",
   "http://www.zillow.com/sunnyvale-ca/home-values/",
   "http://www.zillow.com/cupertino-ca/home-values/",
   "http://www.zillow.com/mountain-view-ca/home-values/",
   "http://www.zillow.com/los-altos-ca/home-values/",
   "http://www.zillow.com/palo-alto-ca/home-values/",
   "http://www.zillow.com/menlo-park-ca/home-values/",
   "http://www.zillow.com/foster-city-ca/home-values/"
   "http://www.zillow.com/san-mateo-ca/home-values/",
   "http://www.zillow.com/south-san-francisco-ca/home-values/",
   "http://www.zillow.com/san-francisco-ca/home-values/",
   "http://www.zillow.com/milpitas-ca/home-values/",
   "http://www.zillow.com/fremont-ca/home-values/",
   "http://www.zillow.com/newark-ca/home-values/",
   "http://www.zillow.com/union-city-ca/home-values/",
   "http://www.zillow.com/hayward-ca/home-values/",
   "http://www.zillow.com/pleasanton-ca/home-values/",
   "http://www.zillow.com/dublin-ca/home-values/",
   "http://www.zillow.com/san-ramon-ca/home-values/",
   "http://www.zillow.com/reno-nv/home-values/"
   
)
print "******************"
print zillow_say
print "******************\n"

dic_x = {}

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
            #print '{0:30s} is\t $ {1}'.format(city, price)
            dic_x[city] = price
			

			
#print dic_x


#dic_x = {'Cupertino': '1,790,600', 'Los Altos': '2,742,700', 'Santa Clara': '957,300', 'Dublin': '745,200', 'Menlo Park': '1,963,100', 'Mountain View': '1,390,500', 'San Jose': '796,400', 'Fremont': '854,900', 'Union City': '693,200', 'Reno': '272,800', 'Newark': '665,200', 'Pleasanton': '935,800', 'San Ramon': '911,800', 'Foster City': '1,352,300', 'Sunnyvale': '1,333,300', 'Palo Alto': '2,482,900', 'South San Francisco': '806,300', 'San Francisco': '1,117,300', 'Milpitas': '809,400'}


n_groups =  len(dic_x)
#print "N = %s" %n_groups 

citys = []
std_women = [0] * n_groups


means_women = []


for key, value in dic_x.iteritems() :
    #means_women.append(int(value.replace(",", "")))
    dic_x[key] = int(value.replace(",", ""))
    #citys.append(key)

for key, value in sorted(dic_x.iteritems(), key=lambda (k,v): (v,k)):
#    print "%s: \t\t\t%s" % (key, value)
    print '{:20} {:>12} $'.format(key,value)
    means_women.append(value)
    dic_x[key] = value
    citys.append(key)


#print citys

price_in_million = []
for divide in means_women:
    temp = float(divide) / 1000000
    price_in_million.append(temp)

#print price_in_million 

fig, ax = plt.subplots()
fig.set_size_inches(9, 8,forward=True)

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects2 = plt.bar(index + bar_width, means_women, bar_width,
                 alpha=opacity,
                 color='#5886c5',
                 yerr=std_women,
                 error_kw=error_config
                 #label='Women'
		 )

for label_list in range(1,len(means_women)+1):
    plt.text(0.96*label_list,  means_women[label_list-1]+10000, "%.2fM" %price_in_million[label_list-1] , ha='center', color='#5d5553', fontsize=8)



plt.xlabel('City', color='#ff6600')

ax = plt.gca()
ax.tick_params(axis='x', colors='#011e60')


plt.ylabel('Middle Price', color='#ff6600')
ax.tick_params(axis='y', colors='#011e60')


plt.title("This report generate on %s-%s-%s" %(date.year,date.month,date.day),  color='#ff6600')
plt.xticks(index + bar_width, citys)

fig.autofmt_xdate()

plt.legend()

plt.tight_layout()
plt.show()

