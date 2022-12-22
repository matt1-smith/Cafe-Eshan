from Ingredients import MENU
from Ingredients import resources
from Ingredients import logo


#
def cls():
    """function to clear the console"""
    print('\n'*10)


def order():
    """gets user input for which beverage they'd like"""
    return input("What would you like? (espresso/latte/cappuccino): ")


def check_levels(water_level, milk_level, coffee_level, req_water, req_milk, req_coffee):
    """checks if there's enough of each ingredient to make the requested drink"""
    if water_level >= req_water and milk_level >= req_milk and coffee_level >= req_coffee:
        return True
    else:
        return False


def receive_payment(beverage, money):
    """processes payment and gives change or refunds if needed"""
    cost = int(MENU[beverage]['cost'])
    print(f"The {beverage} costs ${cost}")
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * .25 + dimes * .1 + nickels * .05 + pennies * .01
    if total > cost:
        change = total - cost
        cls()
        print(f"Your change is {change}.")
        return money + cost, True
    elif total == cost:
        cls()
        print("Payment accepted.")
        return money + cost, True

    else:
        print(f"You did not insert enough money. Your refund is {total}")
        return money, False


def report(water_level, milk_level, coffee_level, money):
    """gives report of ingredient levels and money earned"""
    return print(f"Water: {water_level}ml \nMilk: {milk_level}ml \nCoffee: {coffee_level}ml \n Money: ${money}")


def brew(water_level, milk_level, coffee_level, req_water, req_milk, req_coffee):
    """reduces ingredients by recipe level and brews the beverage"""
    water_level = water_level - req_water
    milk_level = milk_level - req_milk
    coffee_level = coffee_level - req_coffee
    return water_level, milk_level, coffee_level, print("Enjoy your beverage! ☕")


def denim_coffee():
    # machine resources
    water_level = resources['water']
    milk_level = resources['milk']
    coffee_level = resources['coffee']
    money = 0
    power = True
    while power:
        print(logo)
        # receives input from user
        user_order = order()
        # provides ingredients level to user
        if user_order == 'report':
            report(water_level, milk_level, coffee_level, money)
        # refills ingredients to max level
        elif user_order == 'refill':
            water_level = 900
            milk_level = 600
            coffee_level = 300
        # powers off coffee machine
        elif user_order == 'off':
            power = False
        # fulfills users order
        else:
            order_ingredients = MENU[user_order]['ingredients']
            # recipe
            req_water = order_ingredients['water']
            req_milk = order_ingredients['milk']
            req_coffee = order_ingredients['coffee']
            levels_good = check_levels(water_level, milk_level, coffee_level, req_water, req_milk, req_coffee)
            if levels_good:
                payment_result = receive_payment(user_order, money)
                money = payment_result[0]
                payment_good = payment_result[1]
                if payment_good:
                    remaining_level = brew(water_level, milk_level, coffee_level, req_water, req_milk, req_coffee)
                    water_level = remaining_level[0]
                    milk_level = remaining_level[1]
                    coffee_level = remaining_level[2]
            else:
                print("Not enough ingredients. Please choose a different beverage.")


denim_coffee()
