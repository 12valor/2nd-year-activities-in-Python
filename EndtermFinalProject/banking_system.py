# banking_system.py

def read_users(filename="bank_data.txt"):
    users = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, balance = line.strip().split(",")
                users[name] = float(balance)
    except FileNotFoundError:
        pass
    return users

def write_users(users, filename="bank_data.txt"):
    with open(filename, "w") as file:
        for name, balance in users.items():
            file.write(f"{name},{balance}\n")

def add_user(users):
    name = input("Enter new username: ")
    if name in users:
        print("User already exists.")
    else:
        users[name] = 0.0
        print("User added successfully.")

def deposit(users):
    name = input("Enter username: ")
    if name in users:
        amount = float(input("Enter amount to deposit: "))
        users[name] += amount
        print(f"Deposited ${amount:.2f}. New balance: ${users[name]:.2f}")
    else:
        print("User not found.")

def withdraw(users):
    name = input("Enter username: ")
    if name in users:
        amount = float(input("Enter amount to withdraw: "))
        if users[name] >= amount:
            users[name] -= amount
            print(f"Withdrawn ${amount:.2f}. New balance: ${users[name]:.2f}")
        else:
            print("Insufficient balance.")
    else:
        print("User not found.")

def check_balance(users):
    name = input("Enter username: ")
    if name in users:
        print(f"Current balance: ${users[name]:.2f}")
    else:
        print("User not found.")

def search_user(users):
    name = input("Enter username to search: ")
    if name in users:
        print(f"{name} found with balance: ${users[name]:.2f}")
    else:
        print("User not found.")

def main():
    users = read_users()
    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add New User")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Search User")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_user(users)
        elif choice == "2":
            deposit(users)
        elif choice == "3":
            withdraw(users)
        elif choice == "4":
            check_balance(users)
        elif choice == "5":
            search_user(users)
        elif choice == "6":
            write_users(users)
            print("Exiting... Data saved.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
