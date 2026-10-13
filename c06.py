print("Welcome to this vending machine!")

# ==> TASK 1
stock = {"Crisps": 0.9, "Chocolate": 1.2, "Popcorn": 0.7, "Biscuits": 1.4, "Sweets": 1.0}
# ==> TASK 2
funds = 10.0
playing = True
purchased = []

while playing == True:

    print()
    print("1 - Display the available items")
    print("2 - Purchase an item")
    print("3 - Exit the vending machine")
    print()
    choice = int(input("Enter choice (1-3): "))
    print()

    if choice == 1:

        index = 0
        for item in stock:
            index += 1
            print(f"{index} | {item} - £{stock[item]}")
        print(f"You have £{funds}")

    elif choice == 2:

        option = int(input("Enter the number for your snack: "))
        snack = list(stock)[option - 1]
        price = stock[snack]
        if funds - price < 0.0:
            print("You do not have enough money to purchase that snack")
        else:
            # ==> TASK 3
            funds = funds
            # ==> TASK 4
            
            print(f"You have purchased {snack} for £{price}")
            print(f"You have £{funds} remaining")

    elif choice == 3:

        print(f"You have purchased: {purchased}")
        print(f"You have £{funds} left")
        playing = False