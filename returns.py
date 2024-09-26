#Calculating monthly returns for set time horizons 

def returns(df):
    outlier_cutoff = 0.002
    lags = [1, 2, 3, 6, 9, 12]
    for lag in lags:
        df[f'return_{lag}m'] = (
            df['adj close']
            .pct_change(lag)
            .pipe(lambda x: x.clip(lower=x.quantile(outlier_cutoff), upper=x.quantile(1 - outlier_cutoff)))
            .add(1)
            .pow(1 / lag)
            .sub(1)
        )
return df

#Adding to feature set to capture time series dynamics 
aggdata = aggdata.groupby(level=1, group_keys=False).apply(returns)
