#Assigning clusters to form a portfolio for each new month 
def clusters(cl):
  cl['cluster'] = KMeans(n_clusters = 5, random_state=0, init = 'random').fit(cl).labels_
  return cl
  
#Filtering data by clusters
def plot(aggdata):
    cluster0 = aggdata[aggdata['cluster'] == 0]
    cluster1 = aggdata[aggdata['cluster'] == 1]
    cluster2 = aggdata[aggdata['cluster'] == 2]
    cluster3 = aggdata[aggdata['cluster'] == 3]
    cluster4 = aggdata[aggdata['cluster'] == 4]
    plt.scatter(cluster0['rsi'], cluster0['atr'], color='red', label='Cluster 0')
    plt.scatter(cluster1['rsi'], cluster1['atr'], color='blue', label='Cluster 1')
    plt.scatter(cluster2['rsi'], cluster2['atr'], color='green', label='Cluster 2')
    plt.scatter(cluster3['rsi'], cluster3['atr'], color='black', label='Cluster 3')
    plt.scatter(cluster4['rsi'], cluster4['atr'], color='orange', label='Cluster 4')
    plt.xlabel('RSI')
    plt.ylabel('ATR')
    plt.legend()
    plt.grid(True)
  
def create_plots(aggdata):
    plt.style.use('ggplot')
    for date in aggdata.index.get_level_values('date').unique():
        g = aggdata.xs(date, level=0)
#Iterating over unique dates and visualizing      
        plt.figure(figsize=(12, 8)) 
        plt.title(f'Date {date.strftime("%Y-%m-%d")}')
        plot(g)
        plt.show()
