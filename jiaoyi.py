import numpy as np
import pandas as pd
import yfinance as yf

# 获取股票数据
def get_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# 计算均值和标准差
def calculate_mean_std(data, window):
    data['Mean'] = data['Close'].rolling(window=window).mean()
    data['Std'] = data['Close'].rolling(window=window).std()

# 生成交易信号
def generate_signals(data):
    data['Signal'] = np.where(data['Close'] > data['Mean'] + data['Std'], -1, np.nan)
    data['Signal'] = np.where(data['Close'] < data['Mean'] - data['Std'], 1, data['Signal'])
    data['Signal'] = np.where(data['Close'] > data['Mean'], 0, data['Signal'])
    data['Signal'] = data['Signal'].ffill().fillna(0)

# 计算持仓和资金曲线
def calculate_positions(data):
    data['Position'] = data['Signal'].diff()
    data['Position'] = data['Position'].fillna(0)
    data['Position'] = np.where(data['Position'] != 0, data['Signal'], 0)
    data['Position'] = data['Position'].ffill()

    data['Market Return'] = np.log(data['Close'] / data['Close'].shift(1))
    data['Strategy Return'] = data['Market Return'] * data['Position'].shift(1)

    data['Cumulative Market Return'] = np.cumsum(data['Market Return'])
    data['Cumulative Strategy Return'] = np.cumsum(data['Strategy Return'])

# 回测和结果分析
def backtest(data):
    initial_capital = 1000000
    data['Position'] = data['Signal']
    data['Position'] = data['Position'].ffill().fillna(0)
    data['Market Return'] = np.log(data['Close'] / data['Close'].shift(1))
    data['Strategy Return'] = data['Market Return'] * data['Position'].shift(1)
    data['Cumulative Market Return'] = np.cumsum(data['Market Return'])
    data['Cumulative Strategy Return'] = np.cumsum(data['Strategy Return'])

    data['Portfolio Value'] = initial_capital * (1 + data['Cumulative Strategy Return'])
    data['Portfolio Return'] = np.log(data['Portfolio Value'] / data['Portfolio Value'].shift(1))
    data['Portfolio Return'] = data['Portfolio Return'].fillna(0)

    return data

# 主函数
def main():
    symbol = 'AAPL'  # 股票代码
    start_date = '2018-01-01'  # 起始日期
    end_date = '2023-01-01'  # 结束日期
    window = 20  # 均值回归窗口

    # 获取股票数据
    data = get_stock_data(symbol, start_date
