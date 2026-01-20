# Bank Management System

class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")

    def display(self):
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(name, account_number)
            print("Account created successfully")
        else:
            print("Account already exists")

    def get_account(self, account_number):
        return self.accounts.get(account_number)


bank = Bank()

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter account holder name: ")
        acc_no = input("Enter account number: ")
        bank.create_account(name, acc_no)

    elif choice == "2":
        acc_no = input("Enter account number: ")
        account = bank.get_account(acc_no)
        if account:
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        else:
            print("Account not found")

    elif choice == "3":
        acc_no = input("Enter account number: ")
        account = bank.get_account(acc_no)
        if account:
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        else:
            print("Account not found")

    elif choice == "4":
        acc_no = input("Enter account number: ")
        account = bank.get_account(acc_no)
        if account:
            account.display()
        else:
            print("Account not found")

    elif choice == "5":
        print("Thank you for using the bank system")
        break

    else:
        print("Invalid choice")


# Simple E-commerce cart system

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id]["quantity"] += quantity
        else:
            self.items[product.product_id] = {
                "product": product,
                "quantity": quantity
            }
        print("Product added to cart")

    def remove_product(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            print("Product removed from cart")
        else:
            print("Product not found in cart")

    def view_cart(self):
        if not self.items:
            print("Cart is empty")
            return

        total = 0
        for item in self.items.values():
            product = item["product"]
            quantity = item["quantity"]
            cost = product.price * quantity
            total += cost
            print(product.name, "| Price:", product.price, "| Quantity:", quantity, "| Total:", cost)

        print("Cart Total Amount:", total)


products = {
    1: Product(1, "Laptop", 50000),
    2: Product(2, "Phone", 20000),
    3: Product(3, "Headphones", 2000)
}

cart = Cart()

while True:
    print("\n1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for p in products.values():
            print(p.product_id, p.name, p.price)

    elif choice == "2":
        pid = int(input("Enter product id: "))
        qty = int(input("Enter quantity: "))
        if pid in products:
            cart.add_product(products[pid], qty)
        else:
            print("Invalid product id")

    elif choice == "3":
        pid = int(input("Enter product id to remove: "))
        cart.remove_product(pid)

    elif choice == "4":
        cart.view_cart()

    elif choice == "5":
        print("Thank you for shopping")
        break

    else:
        print("Invalid choice")


