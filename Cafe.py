from Ingredients import MENU
from Ingredients import resources

# main program

# TODO user input for which beverage they'd like


def order():
    return input("What would you like? (espresso/latte/cappuccino): ")


# TODO get info about specified drink
# TODO check for ingredient level

# checks if there's enough of each ingredient to make the requested drink
def check_levels(water_level, milk_level, coffee_level, req_water, req_milk, req_coffee):
    if water_level > req_water and milk_level > req_milk and coffee_level > req_coffee:
        return True
    else:
        return False


# TODO ask how many of each coin they insert
# TODO receive payment
# TODO brew the drink and decrease ingredients by proper amount
# TODO able to print report of ingredient levels and money collected
def cafe_eshan():
    # machine resources
    water_level = resources['water']
    milk_level = resources['milk']
    coffee_level = resources['coffee']

    # order
    user_order = order()
    order_ingredients = MENU[user_order]['ingredients']

    # recipe
    req_water = order_ingredients['water']
    req_milk = order_ingredients['milk']
    req_coffee = order_ingredients['coffee']

    levels_good = check_levels(water_level, milk_level, coffee_level, req_water, req_milk, req_coffee)

cafe_eshan()
