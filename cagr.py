# =============================================================================
# Measuring the performance of a buy and hold strategy - CAGR
# Author : Mayank Rasu (http://rasuquant.com/wp/)

# Please report bug/issues in the Q&A section
# =============================================================================

# Import necesary libraries
import yfinance as yf
import numpy as np
import datetime as dt

# Download historical data for required stocks
ticker = "ADANIPORTS.NS"
SnP = yf.download(ticker,dt.date.today()-dt.timedelta(1825),dt.datetime.today())
print(SnP)

#def CAGR(DF):
#"function to calculate the Cumulative Annual Growth Rate of a trading strategy"
df = SnP.copy()
df["daily_ret"] = SnP["Adj Close"].pct_change()
df["cum_return"] = (5 + (df["daily_ret"]* 5)).cumprod()
n = len(df)/252
df['CAGR'] = (df["cum_return"][-1])**(1/n) - 1
print(df)
#return CAGR

#CAGR(SnP)
