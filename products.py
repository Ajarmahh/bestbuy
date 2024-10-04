class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("name cannot be empty.")
        if price < 0:
            raise ValueError("price must be a float.")
        if quantity < 0:
            raise ValueError("quantity shouldn't be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.active = False
        self.active = True

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("we run out of this product.")

        if quantity > self.quantity:
            raise ValueError("Not enough product available.")

        total_price = quantity * self.price
        self.quantity -= quantity
        return total_price


class Store:
    def __init__(self, products_list):
        self.products_list = products_list

    def add_product(self, product):
        self.products_list.append(product)

    def remove_product(self, product):
        self.products_list.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> list:
        active_list = []
        for product in self.products_list:
            if product.is_active():
                active_list.append(product)
        return active_list

    def order(self, shopping_list: list) -> float:
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price



