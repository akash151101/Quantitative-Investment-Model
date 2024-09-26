#Garman-Klass-Yang-Zhang Historical Volatility
df['garman_klass_vol'] = np.sqrt(((np.log(df['high']) - np.log(df['low']))**2)/2 - (2*np.log(2) - 1) * (np.log(df['adj close']) - np.log(df['open']))**2)

#Realtive strength index at a lookback period of 25 
df['rsi'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.rsi(close=x, length=25))

#Lower, middle and upper Bollinger Bands for the log-adjusted closing prices
df['bb_low'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.bbands(close=np.log1p(x), length=25).iloc[:, 0])
df['bb_mid'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.bbands(close=np.log1p(x), length=25).iloc[:, 1])
df['bb_high'] = df.groupby(level=1)['adj close'].transform(lambda x: pandas_ta.bbands(close=np.log1p(x), length=25).iloc[:, 2])

#Calculating the standardized ATR (Average True Rate) to measure volatility 
def atr(data):
  atr = pandas_ta.atr(high = data['high'], low = data['low'], close = data['close'],length=15)
  return atr.sub(atr.mean()).div(atr.std())
df['atr'] = df.groupby(level=1, group_keys=False).apply(atr)

#MACD to analyze momentum 
def macd(close):
    macd = pandas_ta.macd(close = close, length=25).iloc[:,0]
    return macd.sub(macd.mean()).div(macd.std())
df['macd'] = df.groupby(level=1, group_keys=False)['adj close'].apply(macd)

#Dollar Volume for money flow 
df['dollar_volume'] = (df['adj close']*df['volume'])/1e6
