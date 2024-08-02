from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#TODO
# ✅Print report
# ✅check resources
# ✅process coins
# ✅check transaction
# ✅make coffee

coffee_machine = CoffeeMaker()
coffee_machine_menu = Menu()
coin_machine = MoneyMachine()

#espresso_drink = MenuItem("espresso", 50, 0, 18, 1.5)
#latte_drink = MenuItem("latte", 200, 150, 24, 2.5)
#cappucino_drink = MenuItem("cappucino", 250, 100, 24, 3.0)
is_on = True

while is_on:
    choice = input(f"What would you like? {coffee_machine_menu.get_items()}: ")

    if choice == "off":
        is_on = False
        print("Turning the machine OFF...")
        print()

    elif choice == "report":
        coffee_machine.report()
        coin_machine.report()

    else:
        drink = coffee_machine_menu.find_drink(choice)

        if coffee_machine.is_resource_sufficient(drink) :
            if coin_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)




    