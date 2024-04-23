class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product type")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if product.name in self.products:
            self.products[product.name]['amount'] += amount
        else:
            self.products[product.name] = {'product': product, 'amount': amount}

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for product_name in self.products:
                if product_name == identifier:
                    self.products[product_name]['product'].price *= (1 - percent / 100)
        elif identifier_type == 'type':
            for product_name, info in self.products.items():
                if info['product'].type == identifier:
                    info['product'].price *= (1 - percent / 100)
        else:
            raise ValueError("Invalid identifier type")

    def sell_product(self, product_name, amount):
        if product_name not in self.products:
            raise ValueError("Product not found")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.products[product_name]['amount'] < amount:
            raise ValueError("Insufficient stock")
        self.products[product_name]['amount'] -= amount

    def get_income(self):
        income = 0
        for info in self.products.values():
            income += info['product'].price * info['amount']
        return income

    def get_all_products(self):
        return [info['product'] for info in self.products.values()]

    def get_product_info(self, product_name):
        if product_name not in self.products:
            raise ValueError("Product not found")
        return (product_name, self.products[product_name]['amount'])


# Test cases
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)
