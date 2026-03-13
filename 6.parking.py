parking_prices = {
    'First hour': 5000,
    'Additional hour': 3000
}

print('Welcome to J. R. Cars Parking.')
print('\nOur rates are as follows:')
for key, value in parking_prices.items():
    print(f'- {key}: ${value:,} pesos')

while True:
    try:
        hours = int(input('Enter the number of hours you parked: '))
        total_cost = parking_prices['First hour'] + (hours - 1) * parking_prices['Additional hour']
        print(f'\nThe total cost for {hours} hour(s) is: ${total_cost:,} pesos')
        break
    except ValueError:
        print('Error: Please enter a valid number.')