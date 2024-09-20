class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)
        print(f"{item.name} has been added to your cart.")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        print("Items in your cart:")
        for item in self.cart:
            print(f"- {item.name}: ${item.price:.2f}")

    def checkout(self):
        total = sum(item.price for item in self.cart)
        print(f"Total amount: ${total:.2f}")
        self.cart.clear()
        print("Checkout complete! Your cart is now empty.")

class GroceryStore:
    def __init__(self):
        self.items = []
        self.users = {}

    def add_item(self, item):
        self.items.append(item)
        print(f"Item {item.name} added to the store.")

    def register_user(self, username, email):
        if username in self.users:
            print("Username already exists.")
        else:
            user = User(username, email)
            self.users[username] = user
            print(f"User {username} registered successfully.")

    def scan_item(self, username, item_name):
        user = self.users.get(username)
        if not user:
            print("User not found. Please register or log in.")
            return

        item = next((item for item in self.items if item.name == item_name), None)
        if item:
            user.add_to_cart(item)
        else:
            print("Item not found.")

# Function to add items 
def add_items_interactively(store):
    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input(f"Enter price for {name}: "))
        store.add_item(Item(name, price))

# Main program execution
store = GroceryStore()

# Add items interactively
add_items_interactively(store)

# Register a user
username = input("Enter username to register: ")
email = input("Enter email: ")
store.register_user(username, email)

# Scan items for the user
while True:
    item_name = input("Enter item name to add to cart (or 'done' to finish): ")
    if item_name.lower() == 'done':
        break
    store.scan_item(username, item_name)

# View cart and checkout
user = store.users[username]
user.view_cart()
user.checkout()
