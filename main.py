import products
import store


def setup_inventory():
    # setup initial stock of inventory
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = products.SecondHalfPrice("Second Half price!")
    third_one_free = products.ThirdOneFree("Third One Free!")
    thirty_percent = products.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    return store.Store(product_list)


def start(store):
    while True:
        print(f"""
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")

        choice = input("Please choose a number: ")

        if choice == '1':
            print("------")
            # Iterate over all active products in the store, with an index starting from 1
            for index, product in enumerate(store.get_all_products(), start=1):
                print(f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.get_quantity()}")
            print("------")

        elif choice == '2':
            total_quantity = store.get_total_quantity()
            print(f"Total of {total_quantity} items in store\n")

        elif choice == '3':
            order_list = []
            print("------")
            for index, product in enumerate(store.get_all_products(), start=1):
                product_info = f"{index}. {product.name}, Price: ${product.price}, Quantity: {product.get_quantity()}"

                # Check if there is a promotion and include it in the display
                if product.promotion is not None:
                    product_info += f", Promotion: {product.promotion.name}"

                print(product_info)  # Print the product information
            print("------\nWhen you want to finish order, enter empty text.")

            while True:
                product_index = input("\nWhich product do you want? ")
                if product_index == '':
                    break

                quantity = input("What amount do you want? ")

                if quantity == '':
                    break

                try:
                    product_index = int(product_index) - 1  # Adjusting index for 0 based list
                    quantity = int(quantity)
                    if quantity > store.get_total_quantity():
                        print("Unfortunately, we don't have the requested amount")

                    elif 0 <= product_index < len(store.get_all_products()):
                        product = store.get_all_products()[product_index]
                        order_list.append((product, quantity))

                        # This update the quantity we have each time the user enter a number
                        quantity -= quantity
                        if quantity <= 0:
                            print("We run out of this item, try again later")
                        else:
                            print("Product added to list!")

                    else:
                        print("Invalid product number. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

            if order_list:
                try:
                    total_price = store.order(order_list)
                    print(f"********\nOrder made! Total payment: ${total_price}\n")
                except ValueError as e:
                    print(e)

        elif choice == '4':
            break


def main():
    store_instance = setup_inventory()
    start(store_instance)


if __name__ == "__main__":
    main()
