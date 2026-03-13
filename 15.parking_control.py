print('--Parking Lot Control--')

# Rates
car_rate = 4000
moto_rate = 2000

# Counters and accumulators
total_collected = 0
car_count = 0
moto_count = 0

# Vehicle that paid the most
max_payment = 0
max_vehicle = None  # No vehicle yet

# Loop for 8 vehicles
for i in range(1, 9):
    print(f'\nVehicle {i}')

    # License plate input
    plate = input('Enter license plate: ').strip()
    if not plate:
        plate = None  # If empty, store None

    # Vehicle type input
    while True:
        vehicle_type = input('Enter type (car/moto): ').lower()
        if vehicle_type in ('car', 'moto'):
            break
        print('Error: enter "car" or "moto".')

    # Hours parked input
    while True:
        try:
            hours = int(input('Enter hours parked: '))
            if hours <= 0:
                print('Error: hours must be positive.')
                continue
            break
        except ValueError:
            print('Error: enter a valid integer.')

    # Calculate payment
    if vehicle_type == 'car':
        payment = hours * car_rate
        car_count += 1
    else:
        payment = hours * moto_rate
        moto_count += 1

    total_collected += payment

    # Track the vehicle that paid the most
    if payment > max_payment:
        max_payment = payment
        max_vehicle = plate

    print(f'Total to pay: ${payment}')

# Final report
print('\n----Summary----')
print(f'Total collected: ${total_collected}')
print(f'Number of cars: {car_count}')
print(f'Number of motos: {moto_count}')
if max_vehicle is not None:
    print(f'Vehicle that paid the most: {max_vehicle} (${max_payment})')
else:
    print('No vehicles were registered.')