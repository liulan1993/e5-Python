import numpy as np
import pandas as pd
import yfinance as yf  # 用于获取股票价格数据

# 步骤1: 数据获取和处理
symbol = "AAPL"  # 股票代码
start_date = "2010-01-01"  # 起始日期
end_date = "2022-12-31"  # 结束日期

# 使用yfinance获取股票价格数据
data = yf.download(symbol, start=start_date, end=end_date)

# 步骤2: 特征工程
# 计算20日和50日移动平均线
data['MA20'] = data['Close'].rolling(window=20).mean()
data['MA50'] = data['Close'].rolling(window=50).mean()

# 步骤3: 模型构建和训练
# 生成交易信号
data['Signal'] = np.where(data['MA20'] > data['MA50'], 1, -1)

# 步骤4: 模型评估和验证
# 计算每日收益率
data['Return'] = np.log(data['Close'] / data['Close'].shift(1))

# 计算策略累积收益率
data['StrategyReturn'] = data['Return'] * data['Signal'].shift(1)

# 计算策略累积收益
data['CumulativeReturn'] = (1 + data['StrategyReturn']).cumprod()

# 步骤5: 执行交易
# 假设初始资金为100,000美元
initial_capital = 100000

# 计算持有股票的数量
data['Position'] = initial_capital * data['Signal'].shift(1).fillna(0).cumsum()

# 计算现金的数量（初始资金减去持有股票的市值）
data['Cash'] = initial_capital - (data['Close'] * data['Signal'].shift(1).fillna(0)).cumsum()

# 计算总资产的数量（现金加上持有股票的市值）
data['TotalAsset'] = data['Cash'] + (data['Close'] * data['Signal'].shift(1).fillna(0)).cumsum()

# 输出结果
print(data[['Close', 'MA20', 'MA50', 'Signal', 'CumulativeReturn', 'TotalAsset']].tail())
