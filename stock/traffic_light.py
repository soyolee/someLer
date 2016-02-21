from matplotlib.finance import quotes_historical_yahoo_ochl
from matplotlib.finance import fetch_historical_yahoo
from datetime import date
import pandas as pd
import re
import datetime

date = datetime.datetime.now()

def div(stock_symbol):
    today = date.today()
    start = (today.year - year_to_cal, today.month, today.day)
    a = fetch_historical_yahoo(stock_symbol, start, today, cachename=None,dividends=True)
    dd = pd.DataFrame(list(a))
    
    re1='.*?'	# Non-greedy match on filler
    re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
    rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
    sum = 0
    
    #print dd[0][2]
    for i in xrange(dd.shape[0]):    
        m = rg.search(dd[0][i])
        if m:
            if m.group(1) == 'None':
                pass
            else:
                sum += float(m.group(1))
        #print "("+float1+")"+"\n"
    
    return sum/year_to_cal
    
def symbols(stock_symbol):
    today = date.today()
    start = (today.year , today.month, today.day - 1)   # Here we have a bug. If report running on weekend, you will get error because we only minus one day which possible is NOT value market date.
    quotes = quotes_historical_yahoo_ochl(stock_symbol, start, today)
    df = pd.DataFrame(quotes)
    df.columns = [u'Date', u'Open',u'Close',u'High',u'Low',u'Volume']
    #####
    #df.to_csv('stock_%s.csv' %stock_symbol)
    #test = pd.read_csv('stock_FTNT.csv')
    #print "TEST \n "
    #print test
    ##### 
    sum = 0
    
    for i in xrange(df.shape[0]):
        #print "%.2f + %.2f = %.2f" %(sum,df['Close'][i],sum+df['Close'][i])
        sum += df['Close'][i]
    
    return (sum/df.shape[0])


	
def myprint(color,mes):
    if color == 'r':
        fore = 31
    elif color == 'g':
        fore = 32
    elif color == 'b':
        fore = 36
    elif color == 'y':
        fore = 33
    else:
        fore = 37
    color = "\x1B[%d;%dm" % (1,fore)
    return "%s %s\x1B[0m" % (color,mes)
    
if __name__ == '__main__' :
    year_to_cal = 5
    wonderland = ['FTNT',
                  'CTL',
                  'NLY',
				  'AGNC',
				  'ARR',
                  'LVS',
                  'C',
                  'T',
                  'SAP',
                  'VOO',
                  'GPS',
                  'NTI',
                  'SAN',
                  'CVX',
                  'KO',
                  'MCD',
                  'PG',
                  'TGT',
                  'WMT',
                  'VLKPY', 
                  'CHT' ,  
                  'GRMN'	,
                  'ASX'	,
                  'UMC'	,
                  'SPIL'	,
                  'GIGM'	,
                  'TSM'	,
                  'HSBC'
                  ]
    print "\nThis report generate on %s-%s-%s" %(date.year,date.month,date.day)                  
    print "----------------------------------------------"
    for i in wonderland:
        if symbols(i) > div(i)*30   :
            price = myprint("r","%.2f" %symbols(i))
        elif symbols(i) > div(i)*20 :
            price = myprint("y","%.2f" %symbols(i))
        elif symbols(i) > div(i)*15 :
            price = myprint("b","%.2f" %symbols(i))
        else: 
            price = myprint("g","%.2f" %symbols(i))
            
        #print "***********************"
        print "%s\t : \t%s\t\tdiv %.2f\tsuggest buying price %.2f"  %(i,price,div(i),div(i)*15*0.85)
        #print "%s\t : \t%.2f" %(i,float(price))
        #print i +"\t : ",
        #print "div\t%.2f"  %(div(i))
        #print "***********************"
    print "----------------------------------------------"
    
    
