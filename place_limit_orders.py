# Python script to place limit orders for buying and selling cryptocurrencies on the Binance exchange

# Import necessary libraries
import ccxt

# Define API keys
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Define exchange
exchange = ccxt.binance({'apiKey': api_key, 'secret': api_secret})

# Define trading pair
symbol = 'BTC/USDT'

# Define order type
order_type = 'limit'

# Define order parameters
amount = 0.01
price = 50000

# Place buy limit order
buy_order = exchange.create_order(symbol, order_type, 'buy', amount, price)

# Place sell limit order
sell_order = exchange.create_order(symbol, order_type, 'sell', amount, price)

# Print order details
print('Buy order:', buy_order)
print('Sell order:', sell_order)