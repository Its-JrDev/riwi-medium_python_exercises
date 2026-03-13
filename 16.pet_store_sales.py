print('--Pet Store Sales--')

# Categories
categories = ['alimento', 'juguete', 'accesorio']

# Accumulators for each category
sales_alimento = 0
sales_juguete = 0
sales_accesorio = 0

# Loop for 10 sales
for i in range(1, 11):
    print(f'\nSale {i}')

    # Category input
    while True:
        category = input('Enter category (alimento/juguete/accesorio): ').lower()
        if category in categories:
            break
        print('Error: enter a valid category.')

    # Sale value input
    while True:
        try:
            value = float(input('Enter sale value: '))
            if value <= 0:
                print('Error: value must be positive.')
                continue
            break
        except ValueError:
            print('Error: enter a valid number.')

    # Add to the correct accumulator
    if category == 'alimento':
        sales_alimento += value
    elif category == 'juguete':
        sales_juguete += value
    else:
        sales_accesorio += value

# Show results
print('\n----Summary----')
print(f'Total sales for alimento: ${sales_alimento}')
print(f'Total sales for juguete: ${sales_juguete}')
print(f'Total sales for accesorio: ${sales_accesorio}')

# Determine which category generated the most money
max_sales = max(sales_alimento, sales_juguete, sales_accesorio)
if max_sales == sales_alimento:
    print('Category that generated the most money: alimento')
elif max_sales == sales_juguete:
    print('Category that generated the most money: juguete')
else:
    print('Category that generated the most money: accesorio')