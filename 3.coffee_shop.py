menu = {
    1: ("Coffee", 4000),
    2: ("Tea", 3500),
    3: ("Juice", 5000)
}

print('Welcome to The Coffee Spot. Please choose a drink from the menu.')
print('\n----Menu----')
for option, (drink, price) in menu.items():
    print(f'{option}. {drink}: {price}')

while True:
    try:
        option = int(input('\nEnter the number of the drink you want to order: '))
        if option in menu:
            drink, price = menu[option]
            print(f'You have ordered {drink}. The price is {price}.')
        else:
            print('Error: Invalid option. Please enter a number between 1 and 3.')
            continue
        break
    except ValueError:
        print('Error: Please enter a valid number.')

while True:
    try:
        quantity = int(input('\nEnter the quantity you want to order: '))
        if quantity > 0:
            print(f'You have ordered {quantity} drink(s).')
            break
        else:
            print('Error: Quantity must be a positive number.')
    except ValueError:
        print('Error: Please enter a valid number.')

total = quantity * price

print(f'\nTotal to pay: {total:,} pesos.')