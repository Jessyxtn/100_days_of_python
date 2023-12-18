from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

on = True
while on:
    menu_items = menu.get_items()
    selected_drink = input("What would you like? " + f"({menu_items}) ")
    print(selected_drink)
    
    if selected_drink == "report":
        coffee_maker.report()
        money.report()
        
    elif selected_drink == "off":
        on = False

    else:
        drink_item = menu.find_drink(selected_drink)
        if coffee_maker.is_resource_sufficient(drink_item):
            if money.make_payment(drink_item.cost):
                coffee_maker.make_coffee(drink_item)


    
    