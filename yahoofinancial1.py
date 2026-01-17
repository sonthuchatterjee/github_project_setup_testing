import pandas as pd
from yahoofinancials import YahooFinancials as YF
import datetime as dt
import json

beg_date = (dt.date.today() - dt.timedelta(30)).strftime('%Y-%m-%d')
print(beg_date)
end_date = dt.date.today().strftime('%Y-%m-%d')
print(end_date)

close_prices = pd.DataFrame()
data = YF('ADANIPORTS.NS')
#print(data)
json_obj = data.get_historical_price_data(beg_date,end_date,"daily")
#print(json_obj)
print(type(json_obj))
ohlv = json_obj['ADANIPORTS.NS']['prices']
print(ohlv)
df = pd.DataFrame(ohlv)[['formatted_date','close']]
print(df)
print(df.index)
df.set_index('formatted_date',inplace=True)
print(df)
print(df.index)
print(type(df))
close_prices['ADANIPORTS'] = df['close']
print(close_prices)
print(close_prices.index)
