products = [
    {"id": 1, "name": "Laptop", "price": 45000},
    {"id": 2, "name": "Smartphone", "price": 15000},
    {"id": 3, "name": "Headphones", "price": 2000},
    {"id": 4, "name": "Keyboard", "price": 1200},
    {"id": 5, "name": "Mouse", "price": 800},
    {"id": 6, "name": "Charger", "price": 500},
    {"id": 7, "name": "USB Cable", "price": 300},
    {"id": 8, "name": "Backpack", "price": 2500},
    {"id": 9, "name": "Smartwatch", "price": 3500},
    {"id": 10, "name": "Bluetooth Speaker", "price": 4000},
    {"id": 11, "name": "Webcam", "price": 2200},
    {"id": 12, "name": "External Hard Drive", "price": 5500},
    {"id": 13, "name": "Pen Drive 64GB", "price": 900},
    {"id": 14, "name": "Power Bank", "price": 1800},
    {"id": 15, "name": "Printer", "price": 8500},
    {"id": 16, "name": "Router", "price": 2400},
    {"id": 17, "name": "LED Monitor", "price": 12000},
    {"id": 18, "name": "Gaming Mouse", "price": 2500},
    {"id": 19, "name": "Gaming Keyboard", "price": 3500},
    {"id": 20, "name": "Microphone", "price": 2700},
    {"id": 21, "name": "Tripod Stand", "price": 1500},
    {"id": 22, "name": "Tablet", "price": 22000},
    {"id": 23, "name": "Earbuds", "price": 2800},
    {"id": 24, "name": "Desk Lamp", "price": 1600},
    {"id": 25, "name": "Wireless Charger", "price": 2000},
    {"id": 26, "name": "Smart TV", "price": 38000},
    {"id": 27, "name": "Fitness Band", "price": 2100},
    {"id": 28, "name": "Camera", "price": 32000}
]


cart=[]

def view_products(products):
    print("\n All The products are bellow ")
    print("-"*60)
    if not products:
        print("The products list is empty")
        print("-"*60)
    for i in products:
        print(f"ID: {i['id']} | product name is {i['name']} - price is ₹{i['price']} ")
    print('-'*60)


def add_to_cart(products,cart,product_id,product_quantity):
    if len(cart) >= 8:
        print("Cart is full! Maximum 8 items allowed.")
        return
    
    product = None
    for p in products:
        if p["id"] == product_id:
            product = p
            break

    if not product:
        print("Invalid Product ID!")
        return
    
    for items in cart:
        if items["id"]==product_id:
            items["product_quantity"]+=product_quantity
            print(f" Updated quantity for {items['name']}.")
            return

    new_item={
        "id": product["id"],
        "name": product["name"],
        "price": product["price"] *product_quantity,
        "product_quantity": product_quantity
    }

    
    cart.append(new_item)
    print(f" Added {product['name']} (x{product_quantity}) to cart.")



def view_cart(cart):
    if not cart:
        print("\n Your cart is empty!")
        return

    print("\nYour Cart:")
    print("-" * 50)
    total=0
    for worth in cart:
        sub_total=worth['price']*worth['product_quantity']
        total+=sub_total
        print(f"{worth['name']} (x{worth['product_quantity']}) - ₹{worth['price']} each | Subtotal: ₹{sub_total}")
    print("-" * 50)
    print(f"Total Amount: ₹{total}")
    print("-" * 50)


def update_cart(cart, product_id, product_quantity):
    for item in cart:
        if item["id"] == product_id:
            item["product_quantity"] = product_quantity
            print(f" Updated {item['name']} quantity to {product_quantity}.")
            return
    print(" Product not found in cart!")



def remove_from_cart(cart,product_id):
    for items in cart:
        if items['id']==product_id:
            cart.remove(items)
            print(f" Removed {items['name']} from cart.")
            return
    print(" Product not found in cart!")



def check_out(cart):
    if not cart:
        print("\n Cart is empty! Add items before checkout.")
        return
    print("\n===== Checkout =====")
    total=0
    for item in cart:
        sub_total=item["price"]*item["product_quantity"]
        total+=sub_total
        print(f"{item['name']} (x{item['product_quantity']}) - ₹{sub_total}")
    print("---------------------------")
    print(f" Total Bill: ₹{total}")
    print(" Thank you for shopping with us!")
    cart.clear()


# view_products(products)
# add_to_cart(products,cart,5,1)
# add_to_cart(products,cart,9,2)
# view_cart(cart)
# update_cart(cart,9,1)
# # remove_from_cart(cart,5)
# check_out(cart)


while True:
    print("\n===== Shopping Cart =====")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Update Cart")
    print("5. Remove from Cart")
    print("6. Checkout")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        view_products(products)

    elif choice == "2":
        try:
            product_id = int(input("Enter Product ID to add: "))
            quantity = int(input("Enter Quantity: "))
            if quantity <= 0:
                print(" Quantity must be positive.")
            else:
                add_to_cart(products, cart, product_id, quantity)
        except ValueError:
            print("Invalid input! Enter numbers only.")

    elif choice == "3":
        view_cart(cart)

    elif choice == "4":
        try:
            product_id = int(input("Enter Product ID to update: "))
            quantity = int(input("Enter new Quantity: "))
            if quantity <= 0:
                print(" Quantity must be positive.")
            else:
                update_cart(cart, product_id, quantity)
        except ValueError:
            print(" Invalid input! Enter numbers only.")

    elif choice == "5":
        try:
            product_id = int(input("Enter Product ID to remove: "))
            remove_from_cart(cart, product_id)
        except ValueError:
            print(" Invalid input! Enter a valid Product ID.")

    elif choice == "6":
        check_out(cart)

    elif choice == "7":
        print(" Exiting the program. Goodbye!")
        break

    else:
        print(" Invalid choice! Please enter between 1-7.")
