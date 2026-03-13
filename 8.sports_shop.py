products = []
count = 0

print('Accounting System for R. Sports Shop.')

for i in range(1, 3):    
    while True:
        product = input('\nEnter the product you want to evaluate: ').strip().lower().capitalize()
        if not product:
            print('\nError: Name cannot be empty.')
        elif not product.isalpha():
            print('\nError: Product name can only contain letters.')
        else:
            break
    while True:
        try:
            price = float(input('\nEnter the product price: '))
            if price <= 0:
                print('\nError: Price must be positive.')
                continue
            break
        except ValueError:
            print('\nError: Please enter a valid number.')
    products.append({product: price})

for product in products:
    for name, price in product.items():
        if price > 100000:
            count += 1
            print(f'\nThe product "{name}" exceeds $100,000. Its price is ${price:,.2f} pesos.')

print(f'\nThe number of products that exceed $100,000 is {count}.')