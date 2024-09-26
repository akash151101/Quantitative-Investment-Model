# Quantitative-Investment-Model
The Quantitative Investment Model project focuses on building a quantitative investment strategy that leverages advanced data processing, machine learning, and financial models to identify high-potential stocks and optimize portfolio allocation.

## Key components of the project include:

### Momentum Analysis: 
* Used the Relative Strength Index (RSI) to identify stocks with strong momentum, helping to inform buy/sell decisions based on past performance.
* Overbought (RSI > 70): When the RSI rises above 70, the stock is considered overbought. This may indicate that the stock has been over-purchased and is due for a correction or pullback.
* Oversold (RSI < 30): When the RSI falls below 30, the stock is considered oversold, suggesting that it may be undervalued and could potentially rebound.

### Risk Management with Fama-French 5-Factor Model: 
* This model adjusts for various factors (market, size, value, profitability, and investment) to provide a comprehensive risk-adjusted view of stock performance over time.
* The 5-Factor Model provides more accurate predictions of stock returns by including multiple risk dimensions that affect long-term performance.

### Volatility Measurement: 
* Incorporated Average True Range (ATR) alongside other technical indicators to assess stock volatility and categorize risk levels.
* High ATR Values:- Indicate higher volatility, meaning the price is experiencing larger movements within a period.
* Low ATR Values: Indicate lower volatility, meaning the price is moving within a smaller range, suggesting stability or low-risk conditions.

### KMeans Clustering: 
* Applied machine learning algorithms to group stocks based on shared characteristics, creating distinct risk clusters and enabling better decision-making based on risk profiles.


