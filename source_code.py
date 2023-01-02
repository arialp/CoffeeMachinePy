menu = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def ingredient_check(coffee):
    ingredients_ = menu[coffee]["ingredients"]
    count = 0
    for ingredient in ingredients_:
        if resources[ingredient] >= ingredients_[ingredient]:
            count += 1
        else:
            print("Sorry there is not enough " + ingredient + ".")
            return False
    if count == 2 or count == 3:
        if coins():
            for ingredient in ingredients_:
                resources[ingredient] -= ingredients_[ingredient]
            print("Here's your " + coffee + ". Enjoy!")
            return True
        else:
            return False


def coins():
    quarters = int(input("Please insert quarters: "))
    dimes = int(input("Please insert dimes: "))
    nickels = int(input("Please insert nickels: "))
    pennies = int(input("Please insert pennies: "))

    total = float(quarters*.25 + dimes*.1 + nickels*.05 + pennies*.01)
    if total >= menu[coffee]["cost"]:
        resources["money"] += menu[coffee]["cost"]
        change = total - menu[coffee]["cost"]
        if change > 0:
            print("Here's " + str(change.__round__(2)) + " in change")
        return True
    else:
        print("Sorry that's not enough money.")
        return False


while True:
    coffee = input("What would you like? (espresso/latte/cappuccino) ")
    if coffee == "report":
        for resource in resources:
            if resource == "water" or resource == "milk":
                attrib = "ml"
            if resource == "coffee":
                attrib = "gr"
            if resource == "money":
                attrib = "$"
            print(resource + ": " + str(resources[resource]) + attrib)
        input("\nPress Enter to continue...")
    elif coffee == "off" or coffee == "exit":
        print("Shutting down...")
        quit()
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        ingredient_check(coffee)
    else:
        print("Sorry that's not a valid coffee.")
