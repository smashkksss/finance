import yfinance as yf
import matplotlib.pyplot as plt

# 获取苹果公司（AAPL）的历史股票数据
ticker = 'AAPL'
data = yf.download(ticker, start='2024-12-01', end='2023-01-15')

# 计算20日和50日移动平均线
data['SMA_2'] = data['Close'].rolling(window=2).mean()
data['SMA_5'] = data['Close'].rolling(window=5).mean()

# 绘制收盘价和移动平均线
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA_2'], label='2-Day SMA')
plt.plot(data['SMA_5'], label='5-Day SMA')
plt.title('AAPL Stock Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
