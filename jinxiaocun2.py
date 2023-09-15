
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def update_quantity(self, quantity):
        self.quantity += quantity

    def update_price(self, price):
        self.price = price

    def calculate_value(self):
        return self.quantity * self.price


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_value(self):
        total_value = 0
        for product in self.products:
            total_value += product.calculate_value()
        return total_value

    def display_inventory(self):
        for product in self.products:
            print(f"Product: {product.name}, Quantity: {product.quantity}, Price: {product.price}")


inventory = Inventory()

product1 = Product("Apple", 10, 1.5)
product2 = Product("Banana", 5, 0.75)

inventory.add_product(product1)
inventory.add_product(product2)

print("Initial Inventory:")
inventory.display_inventory()

product1.update_quantity(20)
product2.update_price(1.0)

print("\nUpdated Inventory:")
inventory.display_inventory()

print("\nTotal Inventory Value:", inventory.get_total_value())
