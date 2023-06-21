import pandas as pd
from sklearn.linear_model import LinearRegression

# 读取销售数据
data = pd.read_csv('sales_data.csv')

# 提取年份和销售额列
year = data['Year']
sales = data['Sales']

# 计算同比增长率
sales_growth = sales.pct_change() * 100

# 创建一个新的DataFrame来存储年份、销售额和增长率
sales_data = pd.DataFrame({'Year': year, 'Sales': sales, 'Growth': sales_growth})

# 删除第一个年份，因为无法计算同比增长率
sales_data = sales_data.iloc[1:]

# 划分训练集和测试集
train_data = sales_data[sales_data['Year'] < 2022]
test_data = sales_data[sales_data['Year'] >= 2022]

# 提取训练集的特征和目标变量
train_features = train_data[['Year']]
train_target = train_data['Sales']

# 创建线性回归模型
model = LinearRegression()

# 在训练集上训练模型
model.fit(train_features, train_target)

# 预测测试集的销售额
test_features = test_data[['Year']]
predictions = model.predict(test_features)

# 将预测结果添加到测试集中
test_data['Predictions'] = predictions

# 打印预测结果
print(test_data[['Year', 'Sales', 'Predictions']])

# 可视化预测结果
import matplotlib.pyplot as plt

plt.plot(test_data['Year'], test_data['Sales'], label='Actual Sales')
plt.plot(test_data['Year'], test_data['Predictions'], label='Predicted Sales')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Sales Prediction')
plt.legend()
plt.show()
