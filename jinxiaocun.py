import pandas as pd
import matplotlib.pyplot as plt

class Inventory:
    def __init__(self):
        self.products = pd.DataFrame(columns=['Product', 'Cost', 'Price', 'Quantity'])

    def add_product(self, product, cost, price, quantity):
        new_product = {'Product': product, 'Cost': cost, 'Price': price, 'Quantity': quantity}
        self.products = self.products.append(new_product, ignore_index=True)

    def update_price(self, product, new_price):
        self.products.loc[self.products['Product'] == product, 'Price'] = new_price

    def update_quantity(self, product, quantity_change):
        self.products.loc[self.products['Product'] == product, 'Quantity'] += quantity_change

    def analyze_data(self):
        total_cost = self.products['Cost'].sum()
        total_price = self.products['Price'].sum()
        total_quantity = self.products['Quantity'].sum()

        revenue = total_price * total_quantity
        profit = revenue - total_cost

        summary = f"""
        Total Cost: ${total_cost}
        Total Price: ${total_price}
        Total Quantity: {total_quantity}
        Revenue: ${revenue}
        Profit: ${profit}
        """
        print(summary)

    def visualize_data(self):
        self.products.plot(x='Product', y='Quantity', kind='bar')
        plt.title('Inventory Quantity')
        plt.xlabel('Product')
        plt.ylabel('Quantity')
        plt.show()

if __name__ == '__main__':
    inventory = Inventory()

    # 添加产品
    inventory.add_product('Product A', 10, 20, 100)
    inventory.add_product('Product B', 15, 30, 80)
    inventory.add_product('Product C', 8, 18, 120)

    # 更新产品价格
    inventory.update_price('Product B', 35)

    # 更新产品库存
    inventory.update_quantity('Product A', -20)

    # 分析数据
    inventory.analyze_data()

    # 可视化数据
    inventory.visualize_data()
