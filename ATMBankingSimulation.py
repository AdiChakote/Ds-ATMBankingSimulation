balance = 1000
user = {}

def show_balance():
    print(balance)

def deposit_money(amount):
    enter_amount = int(input("Enter Amount to Deposit: "))
    amount += enter_amount
    print(amount)
    print("Money deposited")

def withdraw_money(amount):
    enter_withdraw_money = int(input("Enter Withdraw Amount: "))
    if enter_withdraw_money > amount:
        print("Insufficient Balance")
    else:
        amount -= enter_withdraw_money
        print("Transaction Successful")

user["name"]= input("Name: ")
user["pin"] = int(input("PIN: "))
user["email"] = input("Email: ")
print("Select from options: ")
show_menu = ["Check Balance", "Deposit Money", "Withdraw Money", "Exit"]

for i in show_menu:
    print(i)

option = input("Type Selected Option: ")
if option == "Check Balance":
    enter_pin = int(input("Enter PIN: "))
    if enter_pin == user["pin"]:
        show_balance()
    else:
        print("Wrong PIN")
elif option == "Deposit Money":
    enter_pin = int(input("Enter PIN: "))
    if enter_pin == user["pin"]:
        deposit_money(balance)
    else:
        print("Wrong PIN")
elif option == "Withdraw Money":
    enter_pin = int(input("Enter PIN: "))
    if enter_pin == user["pin"]:
        withdraw_money(balance)
    else:
        print("Wrong PIN")





