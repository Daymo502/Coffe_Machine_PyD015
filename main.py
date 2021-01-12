import menu

available_resources = menu.resources
machine_money = 0.00


def ask_user():
    asking = input("What would you like? (espresso/latte/cappuccino): ").lower()
    return asking


def check_available_resources(recipe):
    can_prepare = True
    missing_ingredients_list = []
    missing_ingredients_text = ": "

    for ingredient in recipe:
        if recipe[ingredient] > available_resources[ingredient]:
            can_prepare = False
            missing_ingredients_list.append(ingredient)

    for missing_ingredient in missing_ingredients_list:
        missing_ingredients_text += missing_ingredient + " "

    return can_prepare, missing_ingredients_text


def process_coins(drink_name, drink_cost):
    print(f"The price for the {drink_name} is {drink_cost}$.")
    print("Please insert coins 🪙")

    q = float(input("how many quarters?: ")) * 0.25
    d = float(input("how many dimes?: ")) * 0.10
    n = float(input("how many nickles?: ")) * 0.05
    p = float(input("how many pennies?: ")) * 0.01

    total_from_coins = q + d + n + p

    if total_from_coins < drink_cost:
        return False, round(total_from_coins, 2)
    elif total_from_coins >= drink_cost:
        global machine_money
        machine_money += drink_cost
        return True, round((total_from_coins - drink_cost), 2)


def update_available_resources(ingredients_dictionary):
    global available_resources
    for ingredient in ingredients_dictionary:
        available_resources[ingredient] -= ingredients_dictionary[ingredient]


def turn_machine_on():
    machine_is_on = True

    while machine_is_on:

        answer = ask_user()

        if answer == "off":
            print("I'll go take a nap 😴")
            machine_is_on = False
        elif answer == "report":
            print(f"""
            Water: {available_resources['water']}
            Milk: {available_resources['milk']}
            Coffee: {available_resources['coffee']}
            Money: {machine_money}
            """)
        elif answer == "espresso" or answer == "latte" or answer == "cappuccino":
            can_make_drink = check_available_resources(menu.MENU[answer]["ingredients"])
            if not can_make_drink[0]:
                print(f"Sorry there is not enough {can_make_drink[1]}")
            else:
                user_coins = process_coins(answer, menu.MENU[answer]["cost"])
                if user_coins[0]:
                    print(f"Here is {user_coins[1]}$ in change")
                    update_available_resources(menu.MENU[answer]["ingredients"])
                    print(f"Your {answer} is ready ☕ Enjoy!")
                else:
                    print(f"Sorry, That's not enough money. {user_coins[1]}$ refunded.")
        else:
            print("This is not a valid 🤦. Try again!")


turn_machine_on()