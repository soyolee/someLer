from matplotlib.finance import quotes_historical_yahoo_ochl
from matplotlib.finance import fetch_historical_yahoo
from datetime import date
import pandas as pd

def div(stock_symbol):
    today = date.today()
    start = (today.year - 5, today.month, today.day)
    a = fetch_historical_yahoo(stock_symbol, start, today, cachename=None,dividends=True)
    dd = pd.DataFrame(list(a))
    return dd
    
def symbols(stock_symbol):
    today = date.today()
    start = (today.year - 5, today.month, today.day)
    quotes = quotes_historical_yahoo_ochl(stock_symbol, start, today)
    df = pd.DataFrame(quotes)
    df.columns = [u'Date', u'Open',u'Close',u'High',u'Low',u'Volume']
     
    sum = 0
    
    a = fetch_historical_yahoo(stock_symbol, start, today, cachename=None,dividends=True)
    dd = pd.DataFrame(list(a))
    #print dd[0]
    
    for i in xrange(df.shape[0]):
        #print "%.2f + %.2f = %.2f" %(sum,df['Close'][i],sum+df['Close'][i])
        sum += df['Close'][i]
    
    return (sum/df.shape[0])*0.85
    
if __name__ == '__main__' :
    
    wonderland = ['FTNT','CTL','NLY','LVS','C','SAP','VOO']
    print "-----------------------"
    for i in wonderland:
        print "***********************"
        print "%s\t : \t%.2f" %(i,symbols(i))
        print i +"\t : \t",
        print div(i)        
        print "***********************"
    print "-----------------------"
    
