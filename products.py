from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity: int) -> float:
        pass


# Percentage Discount Promotion
class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        return product.price * quantity * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        """
        This function checks for pairs of items and always applies the discount to the second item in each pair.
        """
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return (full_price_items * product.price) + (half_price_items * product.price * 0.5)


class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        free_items = quantity // 3
        return (quantity - free_items) * product.price


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("quantity shouldn't be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # No promotion by default

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
        product_info = f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

        # Check if there is a promotion
        if self.promotion is not None:
            product_info += f", Promotion: {self.promotion.name}"

        print(product_info)

    def set_promotion(self, promotion: Promotion):
        self.promotion = promotion

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("we run out of this product.")

        if quantity > self.quantity:
            raise ValueError("Not enough product available.")

        # Apply promotion if available
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        # Decrease quantity after purchase
        self.quantity -= quantity
        return total_price


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self) -> str:
        print(f"{self.name}, Price: {self.price}")


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self) -> str:
        print(f"{self.name}, Price: {self.price}, Max per order: {self.maximum}")





