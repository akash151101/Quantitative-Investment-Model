#Aggregating data to monthly level features in a new dataframe
last_cols = [c for c in df.columns.unique(0) if c not in ['dollar_volume','volume','open', 'high','low','close']]
aggdata = pd.concat(
    [
        df.unstack('ticker')['dollar_volume'].resample('M').mean().stack().to_frame('dollar_volume'),
        df.unstack()[last_cols].resample('M').last().stack('ticker')
    ],
    axis=1
).dropna()

#5 year rolling average and crossectional dollar volume rank
aggdata['dollar_volume']=aggdata['dollar_volume'].unstack('ticker').rolling(5*12).mean().stack()
aggdata['dollar_vol_rank'] = (aggdata.groupby('date')['dollar_volume'].rank(ascending=False))

#Filtering top 150 stocks based on liquidity 
aggdata = aggdata[aggdata['dollar_vol_rank']<150]
