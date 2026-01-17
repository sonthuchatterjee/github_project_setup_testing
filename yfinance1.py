import yfinance as yf
import pandas as pd
import numpy  as np

data = yf.download("ADANIPORTS.NS",start ="2021-07-01", end ="2021-07-26")
#print(data)
#data1 = yf.download("ADANIPORTS.NS", period = "1mo", interval = "15m")
#print(data1)
#print(type(data1))
#print(data1.index)
#data1.to_csv('yfinance1.csv')
data2 = data.copy()
#print(data2)
#data2['EMA'] = data2['Close'].ewm(span=5,min_periods=5).mean()
#data2['SMAsum'] = data2['Close'].rolling(window=5,min_periods=5).sum()
#data2['SMAavg'] = data2['Close'].rolling(window=5,min_periods=5).mean()
#data2['SMAstd'] = data2['Close'].rolling(window=5,min_periods=5).std()
#data2.dropna(inplace=True)
#print(data2)
#d = data2.iloc[3,4]
#print(d)
data2['change'] = data2['Close'] - data2['Close'].shift(1)
data2['gain'] = np.where(data2['change'] >= 0,abs(data2['change']),0)
data2['loss'] = np.where(data2['change'] <= 0,abs(data2['change']),0)
#data2['Avg Gain'] = np.NaN
#data2['Avg Loss'] = np.NaN
print(type(data2['loss']))
listt = list()
listt.append(data2['loss'].tolist()[5])
print(listt)
print(type(listt))
print(listt.index)
'''data2.reset_index(inplace = True)
#print(data2.index)
print(data2)
print(data2.index)

dataa = data2['Close'].diff().dropna
up = dataa.clip(lower=0)
down = -1*dataa.clip(upper=0)
print(dataa)
print(up)
print(down)
#dat = data2.index.tolist()
#print(dat)

for i in range(len(data2)):
    if i < 14:
     data2.iloc[int(i),10] = np.NaN
     data2.iloc[int(i),11] = np.NaN
    elif i == 14:
     data2.iloc[int(i),10] = data2.iloc[int(i),8].rolling(window=14,min_periods=14).mean()
     data2.iloc[int(i),11] = data2.iloc[int(i),9]
    data2.iloc[int(i),10] = data2['gain'].rolling(window=14,min_periods=14).mean()
     data2.iloc[int(i),11] = data2['loss'].rolling(window=14,min_periods=14).mean()
    else:
     data2.iloc[int(i),10] = (data2.iloc[int(i),10].shift(1) * 13 + data2['gain'])/14
     data2.iloc[int(i),11] = (data2.iloc[int(i),11].shift(1) * 13 + data2['loss'])/14
print(data2)'''
