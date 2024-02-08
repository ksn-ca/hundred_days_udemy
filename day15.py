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

money_in_machine = 0.0

def check_resources(drink):
    drink_req = MENU[drink]['ingredients']
    
    sufficient_amt = True
    insufficient_resources = []

    for dr in drink_req:
        for mr in resources:
            if dr == mr:
                if resources[mr] < drink_req[dr]:
                    sufficient_amt = False
                    insufficient_resources.append(mr)

    return [sufficient_amt, insufficient_resources]

def count_coins(q, d, n, p):
    return (q*0.25 + d*0.1 + n*0.05 + p*0.01)

def print_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money_in_machine}')


def deduct_ingredients(drink):
    drink_req = MENU[drink]['ingredients']
    
    global resources
    for dr in drink_req:
        for mr in resources:
            if dr == mr:
                resources[mr] -= drink_req[dr]

on = True
while on:
    user_choice = input('What would you like? (espresso, latte, capuccino): ').lower()
    
    if user_choice == 'off':
        on = False
    elif user_choice == 'report':
        print_report()
    elif user_choice not in [*MENU]:
        print('This product is not on the menu, try again.')
    else:
        resource_check = check_resources(user_choice)
        
        if resource_check[0]:
            print('Please insert coins.')
            
            quarters = int(input('# of quarters: '))
            dimes = int(input('# of dimes: '))
            nickles = int(input('# of nickles: '))
            pennies = int(input('# of pennies: '))

            total = count_coins(quarters, dimes, nickles, pennies)

            drink_cost = MENU[user_choice]['cost']

            if total >= drink_cost:
                print(f'{total} {drink_cost}')

                money_in_machine += drink_cost

                if total > drink_cost:
                    print(f'Here is {round(total - drink_cost, 2)} in change.')

                deduct_ingredients(user_choice)

                print(f'Here is your {user_choice}. Enjoy!')
            else:
                print('Sorry, that is not enough money. Money refunded.')
        else:
           print(f'Sorry, there is not enough {(", ".join(resource_check[1]))}')
