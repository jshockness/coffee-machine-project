MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def enough_resources(order_ingredients):
    """Returns True if enough ingredients to make order, False if ingredients insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there's not enough {item}.")
            return False
    return True

def count_coins():
    """Returns the total calculated amount frm coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def enough_money(money_received, drink_cost):
    """Return True when the payment is sufficient, or False if money insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change: ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money {money_received} refunded.")
        return False

def make_drink(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name}.")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money : {profit}")
    else:
        drink = MENU[choice]
        if enough_resources(drink["ingredients"]):
            payment = count_coins()
            if enough_money(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])

