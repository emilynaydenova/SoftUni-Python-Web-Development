from project.product import Product

class ProductRepository:
    def __init__(self):
        self.products = list()

    @property
    def count(self):
        return len(self.products)

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        prod = [p for p in self.products if p.name == product_name]
        if prod:
            return prod[0]

    def remove(self, product_name):
        prod = [p for p in self.products if p.name == product_name]
        if prod:
            self.products.remove(prod[0])

    def __repr__(self):
        result = [f'{p.name}: {p.quantity}' for p in self.products]
        return '\n'.join(result)

