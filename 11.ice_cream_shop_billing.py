print('--Billing System: Ice Cream Flavours--')

products = {
    'Cone': 3000,
    'Cup': 4000,
    'Banana Split': 9000
}

count_cone = 0
count_cup = 0
count_b_split = 0

customers = 1
total_money = 0

product_list = list(products.keys())

def product_errors():
    try:
        product = int(input('\nEnter the number of the desired product: ')) - 1
        if product < 0:
            print('Error: Number must be positive.')
            return product_errors()
        elif product >= len(product_list):
            print('Error: Product does not exist.')
            return product_errors()
        return product
    except ValueError:
        print('Error: Please enter an integer.')
        return product_errors()
    
def quantity_errors():
    try:
        quantity = int(input('\nEnter the quantity of the desired product: '))
        if quantity < 0:
            print('Error: Quantity must be positive.')
            return quantity_errors()
        return quantity
    except ValueError:
        print('Error: Please enter an integer.')
        return quantity_errors()
    
def validate_next():
    valid = input('\nDo you want to continue entering orders? (Yes | No): ').lower()
    if valid == 'yes':
        return True
    elif valid == 'no':
        return False
    else:
        print('\nError: Please enter a valid response.')
        return validate_next()
    
while True:
    print("\nAvailable products:")
    for index, name in enumerate(product_list):
        print(f"{index + 1}. {name} - ${products[name]}")
    product_index = product_errors()
    
    amount = quantity_errors()
    
    if product_index == 0:
        count_cone += amount
    elif product_index == 1:  
        count_cup += amount
    elif product_index == 2:
        count_b_split += amount

    product_name = product_list[product_index]
    total = amount * products[product_name]
    total_money += total
    
    print(f'\nCustomer {customers}')
    print(f'\nProduct: {product_name}')
    print(f'Quantity: {amount}')
    print(f'Total: {total:,}')

    if not validate_next():
        break
    customers += 1
    
print('\n----Closure----')
print(f'Total sold: {total_money:,}')
print(f'Customers served: {customers}')

if count_cone > count_cup and count_cone > count_b_split:
    print(f'Most sold product: {product_list[0]}')
elif count_cup > count_cone and count_cup > count_b_split:
    print(f'Most sold product: {product_list[1]}')
elif count_b_split > count_cone and count_b_split > count_cup:
    print(f'Most sold product: {product_list[2]}')
else:
    print('There is a tie between the most sold products.')