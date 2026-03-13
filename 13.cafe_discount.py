print('--Café Billing System--')

# Products and prices
products = {
    'coffee': 4000,
    'cappuccino': 7000,
    'cake': 6000
}

product_list = list(products.keys())
total_day = 0
customer = 1

def product_errors():
    try:
        product = int(input('\nEnter the number of the desired product (or 0 to finish): '))
        if product < 0 or product > len(product_list):
            print('Error: invalid number.')
            return product_errors()
        return product
    except ValueError:
        print('Error: please enter an integer.')
        return product_errors()

def quantity_errors():
    try:
        quantity = int(input('Enter the quantity: '))
        if quantity <= 0:
            print('Error: quantity must be positive.')
            return quantity_errors()
        return quantity
    except ValueError:
        print('Error: please enter an integer.')
        return quantity_errors()

# Customer loop
while True:
    print(f'\nCustomer {customer}')
    total_customer = 0
    
    while True:
        print("\nAvailable products:")
        for idx, name in enumerate(product_list):
            print(f"{idx + 1}. {name} - ${products[name]}")
        print("0. Finish order")

        product_index = product_errors()
        if product_index == 0:
            break

        product_name = product_list[product_index - 1]
        amount = quantity_errors()
        total_customer += products[product_name] * amount

    if total_customer == 0:
        print("No products were ordered.")
    else:
        # Apply discount if total > 20000
        if total_customer > 20000:
            total_customer *= 0.9
            print(f'Total with 10% discount: ${int(total_customer)}')
        else:
            print(f'Total to pay: ${int(total_customer)}')

        total_day += total_customer
        customer += 1

    another = input('\nDo you want to register another customer? (Yes/No): ').lower()
    if another == 'no':
        break

print('\n----End of Day----')
print(f'Total sales for the day: ${int(total_day)}')
print(f'Total customers served: {customer - 1}')