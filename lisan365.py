# 导入所需的库
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# 读取用户数据集
data = pd.read_csv('user_data.csv')

# 定义特征和目标变量
features = data[['age', 'gender', 'purchase_history', 'income']]
target = data['user_segment']

# 将分类变量转换为数字编码（如果有需要）
# gender_mapping = {'male': 0, 'female': 1}
# features['gender'] = features['gender'].map(gender_mapping)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# 创建决策树模型
model = DecisionTreeClassifier()

# 拟合模型
model.fit(X_train, y_train)

# 在测试集上进行预测
predictions = model.predict(X_test)

# 打印预测结果
print(predictions)
