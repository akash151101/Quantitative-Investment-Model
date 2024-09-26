#Using our clusters to find high momentum stocks over a set time period
def find_highest_momentum_stocks(aggdata):
    end_date = aggdata.index.get_level_values('date').max()
    start_date = end_date - pd.DateOffset(months=3)  
    recent_data = aggdata[(aggdata.index.get_level_values('date') >= start_date) & (aggdata.index.get_level_values('date') <= end_date)]

#Calculating average RSI for each stock over the last 3 months
    recent_rsi = recent_data.groupby('ticker')['rsi'].mean()
    sorted_stocks = recent_rsi.sort_values(ascending=False)

#Identifying top 20%, bottom 20%, and middle 60% momentum stocks
    top_20_cutoff = sorted_stocks.quantile(0.8)
    bottom_20_cutoff = sorted_stocks.quantile(0.2)
    risk_labels = sorted_stocks.apply(
        lambda x: 'Green' if x >= top_20_cutoff else ('Red' if x <= bottom_20_cutoff else 'Grey'))

#Merging risk labels back into the rsi dataframe and creating stick to store indicators
    recent_data = recent_data.join(risk_labels.rename('risk'), on='ticker')
    stick = pd.DataFrame({
        'stock': risk_labels.index,
        'risk': risk_labels.values
    })

    return recent_data, stick
    
#Performing KMeans clustering with 3 clusters

def cluster_risk_groups(aggdata):
    features = aggdata[['rsi', 'atr']]
    kmeans = KMeans(n_clusters=3, random_state=42)
    aggdata['cluster'] = kmeans.fit_predict(features)

    return aggdata
    
#Plotting a risk cluster, color coded based on momentum 
def plot_with_risk_clusters(aggdata):
    colors = {'Green': 'green', 'Red': 'red', 'Grey': 'grey'}
        for risk_category, color in colors.items():
        cluster_data = aggdata[aggdata['risk'] == risk_category]
        plt.scatter(cluster_data['rsi'], cluster_data['atr'], color=color, label=risk_category)

#Legend
    plt.xlabel('RSI')
    plt.ylabel('ATR')
    plt.legend()
    plt.grid(True)
    plt.title('Risk Clusters Based on Momentum')

#Clustering risk groups 
def sticks(aggdata):
    plt.style.use('ggplot')
    recent_data, stick = find_highest_momentum_stocks(aggdata)
    clustered_data = cluster_risk_groups(recent_data)
    plt.figure(figsize=(12, 8))
    plot_with_risk_clusters(clustered_data)
    plt.show()
