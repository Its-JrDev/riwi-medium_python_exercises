print('--Sports Clothing Store: Inventory Check--')

# Counters for stock levels
out_of_stock = 0
low_stock = 0
normal_stock = 0

# Loop for 10 products
for i in range(1, 11):
    print(f'\nProduct {i}')

    # Product name input
    while True:
        name = input('Enter product name: ').strip()
        if name:
            break
        print('Error: name cannot be empty.')

    # Quantity input
    while True:
        try:
            quantity = int(input('Enter quantity available: '))
            if quantity < 0:
                print('Error: quantity cannot be negative.')
                continue
            break
        except ValueError:
            print('Error: enter a valid integer.')

    # Classify stock level
    if quantity == 0:
        stock_level = 'out of stock'
        out_of_stock += 1
    elif 1 <= quantity <= 5:
        stock_level = 'low stock'
        low_stock += 1
    else:
        stock_level = 'normal stock'
        normal_stock += 1

    print(f'Stock level for {name}: {stock_level}')

# Final summary
print('\n----Summary----')
print(f'Products out of stock: {out_of_stock}')
print(f'Products with low stock: {low_stock}')
print(f'Products with normal stock: {normal_stock}')