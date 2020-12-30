
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def start():

    def print_report():
        for key, val in resources.items():
            product = key
            amount = val
            print(f"{product} : {amount}")

    print("\nDRINKS MENU")
    for k, v in MENU.items():
        beverage = k
        price = v["cost"]
        print(f"{beverage} : £{price}")

    user_input = input("What would you like?\n")
    if user_input == "off":
        print("The process has stopped.")
        return
    elif user_input == "report":
        print_report()


start()


# def check_resources():
