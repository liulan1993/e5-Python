import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# 读取CSV文件
data = pd.read_csv('orders.csv')

# 查看数据
print(data.head())
# 将日期列转换为月份
data['Month'] = pd.to_datetime(data['OrderDate']).dt.month

# 查看更新后的数据
print(data.head())
# 准备数据
X = data[['Month']].values
y = data['Sales'].values

# 拆分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 预测销量
y_pred = model.predict(X_test)

# 打印预测结果
print('预测销量:', y_pred)
# 创建未来12个月的月份数据
future_months = np.arange(data['Month'].max() + 1, data['Month'].max() + 13).reshape(-1, 1)

# 预测未来12个月的销量
future_sales = model.predict(future_months)

# 打印预测结果
print('未来12个月的销量预测:', future_sales)
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 读取CSV文件
data = pd.read_csv('data.csv')

# 准备数据
X = data[['Feature1', 'Feature2']].values
y = data['Target'].values

# 拆分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 预测
y_pred = model.predict(X_test)

# 打印预测结果
print('预测值:', y_pred)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print('均方误差 (MSE):', mse)
print('决定系数 (R^2):', r2)
