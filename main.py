
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
    "water": 0,
    "milk": 200,
    "coffee": 100,
}


def start():

    def restart():
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
        restart()


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
            print("Not enough water")
            return False
        elif drink_requirements["coffee"] >= resources["coffee"]:
            print("Not enough coffee")
            return False
        elif drink_requirements["milk"] >= resources["milk"]:
            print("Not enough milk")
            return False
        else:
            print("satis")
            return True


    print("\nDRINKS MENU")
    for k, v in MENU.items():
        beverage = k
        price = v["cost"]
        print(f"{beverage} : £{price}")

    user_input = input("What would you like?\n")
    if user_input in INPUTS:
        res_check(user_input)
    elif user_input == "off":
        print("The process has stopped.")
        return
    elif user_input == "report":
        print_report()
    else:
        print("Invalid input")
        restart()




start()
