import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import talib

# Load data
df = pd.read_csv('crypto_data.csv')

# Calculate moving averages
df['MA20'] = talib.SMA(df['Close'], timeperiod=20)
df['MA50'] = talib.SMA(df['Close'], timeperiod=50)

# Calculate RSI
df['RSI'] = talib.RSI(df['Close'], timeperiod=14)

# Calculate Bollinger Bands
df['upper'], df['middle'], df['lower'] = talib.BBANDS(df['Close'], timeperiod=20, nbdevup=2, nbdevdn=2)

# Plot the data
plt.figure(figsize=(12,6))
plt.plot(df['Close'], label='Close')
plt.plot(df['MA20'], label='MA20')
plt.plot(df['MA50'], label='MA50')
plt.legend()
plt.show()

# Identify trading opportunities
df['Signal'] = np.where((df['Close'] > df['MA20']) & (df['Close'] > df['MA50']) & (df['RSI'] < 30) & (df['Close'] < df['lower']), 'Buy', '')
df['Signal'] = np.where((df['Close'] < df['MA20']) & (df['Close'] < df['MA50']) & (df['RSI'] > 70) & (df['Close'] > df['upper']), 'Sell', df['Signal'])

# Print the trading signals
print(df[['Date', 'Close', 'MA20', 'MA50', 'RSI', 'upper', 'middle', 'lower', 'Signal']])
