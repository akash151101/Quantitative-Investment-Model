#Using Fama French Factors to assess risk return profile + Rolling factor betas
ffdata = web.DataReader("F-F_Research_Data_5_Factors_2x3", "famafrench", start="2015")[0].drop("RF", axis=1)
ffdata.index = ffdata.index.to_timestamp()
ffdata.index = ffdata.index.tz_localize('UTC')

#Resampling monthly and normalizing the values 
ffdata = ffdata.resample("M").last().div(100)
ffdata.index.name = 'date'
ffdata = ffdata.join(aggdata['return_1m']).sort_index()

#Dropping the stocks with less than 6 months of data
x = ffdata.groupby(level=1).size()
valid_stocks = x[x >= 6]
ffdata = ffdata [ffdata.index.get_level_values('ticker').isin(x.index)]
ffdata['RFB'] = ffdata[['Mkt-RF', 'SMB', 'HML', 'RMW', 'CMA']].mean(axis=1)

#Shifting the rolling factor betas forward by one month
ffdata['RFB'] = ffdata.groupby(level='ticker')['RFB'].shift(-1)
keep = ['RFB', 'SMB', 'HML', 'RMW', 'CMA']
existing = [col for col in keep if col in ffdata.columns]
#Filtering the dataframe to keep only the desired columns and imputing missing values with mean
ffdata = ffdata[existing]
keep = ['RFB', 'SMB', 'HML', 'RMW', 'CMA']
ffdata.loc[:, keep] =  ffdata.groupby('ticker', group_keys = False)[keep].apply(lambda x: x.fillna(x.mean()))
