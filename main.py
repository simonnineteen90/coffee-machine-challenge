
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

INPUTS = ["latte", "espresso", "cappuccino"]

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def start():

    def restart():
        """
        Ask user if they want to restart programme
        """

        restart = input("Press 'R' to restart or 'Q' to quit\n").lower()
        if restart == "r":
            start()
        else:
            return False

    def print_report():
        """
        Gives info of what resources are available

        """
        for key, val in resources.items():
            product = key
            amount = val
            print(f"{product} : {amount}")
        start()

    def res_check(drink_name):
        """
        Takes one paramater of drink type, then checks if there are enough resources to make the drink according to ingredients in menu dictionary
        """
        all_drink_resources = MENU[drink_name]
        drink_res = all_drink_resources["ingredients"]
        water = drink_res["water"]
        coffee = drink_res["coffee"]
        if drink_name != "espresso":
            milk = drink_res["milk"]
        else:
            milk = 0
        drink_requirements = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }
        if drink_requirements["water"] >= resources["water"]:
            print("Not enough water! Stopping machine.")
            return False
        elif drink_requirements["coffee"] >= resources["coffee"]:
            print("Not enough coffee! Stopping machine.")
            return False
        elif drink_requirements["milk"] >= resources["milk"]:
            print("Not enough milk! Stopping machine.")
            return False
        else:
            print("Resources satis")
            return True

    def process_coins(drink_price):
        """
        Asks user how many of each coin inputted then calculates if correct amount has been paid for selected drink.
        :param drink_price:
        :return:
        """
        quarters = int(input("How many quarters: \n")) * .25
        dimes = int(input("How many dimes: \n")) * .1
        nickles = int(input("How many nickles: \n")) * .05
        pennies = int(input("How many pennies: \n")) * .01
        coins = [quarters, dimes, nickles, pennies]
        total_coins = round(sum(coins), 2)

        if total_coins >= drink_price:
            print(f"You have entered ${total_coins}, drink price is ${drink_price}: satis.")
            if total_coins > drink_price:
                overpaid = round((total_coins - drink_price), 2)
                print(f"You have overpaid. Refunding ${overpaid}.")
            return True
        else:
            print(
                f"You have entered ${total_coins}, drink price is ${drink_price}: Not enough coins. ${total_coins} refunded.")
            return False

    def make_coffee(price, user_input):
        """
        update the resources by adding the price and decucting the coffee/milk/water
        :param price:
        :param user_input:
        :return:
        """
        resources["money"] += price
        resources["water"] -= MENU[user_input]["ingredients"]["water"]
        resources["coffee"] -= MENU[user_input]["ingredients"]["coffee"]
        if user_input != "espresso":
            resources["milk"] -= MENU[user_input]["ingredients"]["milk"]
        print(f"Here is your {user_input} Enjoy!")


    # process starts here
    print("\nDRINKS MENU")
    for k, v in MENU.items():
        beverage = k
        price = v["cost"]
        print(f"{beverage} : £{price}")

    user_input = input("What would you like?\n")
    if user_input in INPUTS:
        price = MENU[user_input]["cost"]
        if res_check(user_input):
            print(f"price is equal to: {price}")
            if process_coins(price):
                make_coffee(price, user_input)
                restart()


    elif user_input == "off":
        print("The process has stopped.")
        return
    elif user_input == "report":
        print_report()
    else:
        print("Invalid input")
        restart()




start()




