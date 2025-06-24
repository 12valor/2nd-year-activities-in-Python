class CusInfo:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Define the POS class
class POS:
    def __init__(self, prod_name, price, quantity):
        self.prod_name = prod_name
        self.price = price
        self.quantity = quantity

    def total_sales(self):
        return self.price * self.quantity

    def discount(self, customer):
        if customer.age >= 60:
            return self.total_sales() * 0.03
        else:
            return 0

    def net_cost(self, customer):
        return self.total_sales() - self.discount(customer)

    def change(self, amount_paid, customer):
        return amount_paid - self.net_cost(customer)

# Main program
if __name__ == "__main__":
    # Input customer info
    name = input("Enter customer name: ")
    age = int(input("Enter customer age: "))
    customer = CusInfo(name, age)

    # Input product info
    prod_name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))
    product = POS(prod_name, price, quantity)

    # Calculations
    total = product.total_sales()
    discount_amount = product.discount(customer)
    net = product.net_cost(customer)

    # Input amount paid
    amount_paid = float(input("Enter amount paid: "))

    # Calculate change
    change_amount = product.change(amount_paid, customer)

    # Display all info
    print("\n--- Transaction Details ---")
    print(f"Customer Name: {customer.name}")
    print(f"Customer Age: {customer.age}")
    print(f"Product Name: {product.prod_name}")
    print(f"Product Price: {product.price:.2f}")
    print(f"Product Quantity: {product.quantity}")
    print(f"Total Sales: {total:.2f}")
    print(f"Discount: {discount_amount:.2f}")
    print(f"Net Cost: {net:.2f}")
    print(f"Amount Paid: {amount_paid:.2f}")
    print(f"Change: {change_amount:.2f}")
    print("----------------------------")
