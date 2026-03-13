print('--Hair Salon Daily Agenda--')

# Services
services = ['haircut', 'brushing', 'dye']

# Counters for each service
count_haircut = 0
count_brushing = 0
count_dye = 0

# Accumulator for total daily revenue
total_day = 0

# Loop for 7 clients
for i in range(1, 8):
    print(f'\nClient {i}')

    # Name input
    while True:
        name = input('Enter client name: ').strip()
        if name:
            break
        print('Error: name cannot be empty.')

    # Service input
    while True:
        service = input('Enter service (haircut/brushing/dye): ').lower()
        if service in services:
            break
        print('Error: enter a valid service.')

    # Payment input
    while True:
        try:
            payment = float(input('Enter amount paid: '))
            if payment <= 0:
                print('Error: amount must be positive.')
                continue
            break
        except ValueError:
            print('Error: enter a valid number.')

    # Add to total revenue
    total_day += payment

    # Increment service counters
    if service == 'haircut':
        count_haircut += 1
    elif service == 'brushing':
        count_brushing += 1
    else:
        count_dye += 1

# Final results
print('\n----Summary----')
print(f'Total revenue for the day: ${total_day}')
print(f'Clients who requested haircut: {count_haircut}')
print(f'Clients who requested brushing: {count_brushing}')
print(f'Clients who requested dye: {count_dye}')

# Determine most requested service
max_count = max(count_haircut, count_brushing, count_dye)
if max_count == count_haircut:
    print('Most requested service: haircut')
elif max_count == count_brushing:
    print('Most requested service: brushing')
else:
    print('Most requested service: dye')