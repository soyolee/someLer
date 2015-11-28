from matplotlib.finance import quotes_historical_yahoo_ochl
import matplotlib.pyplot as plt
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-2, today.month, today.day)
quotes = quotes_historical_yahoo_ochl('MSFT', start, today)
attributes = ['date','open','close','high','low','volume']
quotesdf = pd.DataFrame(quotes, columns = attributes)

list1 = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = date.strftime(x, '%y/%m/%d')
    list1.append(y)
quotesdf.index = list1
quotesdf = quotesdf.drop(['date'], axis = 1 )

#print quotesdf.ix['14/01/30':'14/02/10',['open', 'close']]
#print quotesdf['14/06/01': '14/12/31']['close' > 49]
list1 = []
tmpdf = quotesdf['14/01/01':'14/12/31']
for i in range(0, len(tmpdf)):
    list1.append(int(tmpdf.index[i][3:5]))
    
tmpdf['month'] = list1

#tmpdf.groupby('month')
openMS = tmpdf.groupby('month').mean().open
listopen = []
for i in range(1, 13):
    listopen.append(openMS[i])
#plt.plot(openMS.index, listopen) 
plt.scatter(tmpdf.close - tmpdf.open, tmpdf.volume)
plt.show()
#print tmpdf
#print tmpdf[ tmpdf.close > tmpdf.open]['month'].value_counts()

#print quotesdf[u'14/01/01':u'14/12/31'].sort_values(by='close', ascending=False)[:5]
#print quotesdf['14/1/1':'14/5/31'].sort_values(by='volume') 
#print quotesdf