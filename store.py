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