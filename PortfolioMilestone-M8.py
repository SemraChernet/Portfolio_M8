class ShoppingList:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.item_name == item.item_name:
                if item.item_quantity != 0:
                    cart_item.item_quantity = item.item_quantity
                if item.item_price != 0:
                    cart_item.item_price = item.item_price
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: Description")


def print_menu(cart):
    menu = (
        "MENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
        "Choose an option:"
    )
    choice = ""
    while choice != "q":
        print(menu)
        choice = input()
        if choice == "a":
            print("ADD ITEM TO CART")
            name = input("Enter the item name:\n")
            desc = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            item = ShoppingList(name, price, quantity)
            cart.add_item(item)
        elif choice == "r":
            print("REMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)
        elif choice == "c":
            print("CHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            item = ShoppingList(name, quantity=quantity)
            cart.modify_item(item)
        elif choice == "i":
            print("OUTPUT ITEMS' DESCRIPTIONS")
            cart.print_descriptions()
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            cart.print_total()


if __name__ == "__main__":
    # Step 7
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")
    
    # Create a ShoppingCart object
    cart = ShoppingCart(customer_name, current_date)

    
    print_menu(cart)
