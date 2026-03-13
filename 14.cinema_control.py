print('--Cinema Room Control--')

# Ask for total room capacity
while True:
    try:
        capacity = int(input('Enter the total capacity of the cinema room: '))
        if capacity <= 0:
            print('Error: capacity must be positive.')
            continue
        break
    except ValueError:
        print('Error: enter a valid integer.')

# Initialize counters
total_people = 0
children = 0
adults = 0
seniors = 0

# Register people until the room is full
while total_people < capacity:
    print(f'\nPerson {total_people + 1}')

    while True:
        try:
            age = int(input('Enter age: '))
            if age < 0:
                print('Error: age cannot be negative.')
                continue
            break
        except ValueError:
            print('Error: enter a valid integer.')

    # Classify age group
    if age <= 12:
        children += 1
    elif age <= 64:
        adults += 1
    else:
        seniors += 1

    total_people += 1

    # Ask if more people will enter (optional, if room not full)
    if total_people < capacity:
        more = input('Is there another person? (Yes/No): ').lower()
        if more == 'no':
            break

# Final results
print('\n----Summary----')
print(f'Total people entered: {total_people}')
print(f'Children: {children}')
print(f'Adults: {adults}')
print(f'Seniors: {seniors}')

if total_people == capacity:
    print('The cinema room is full.')
else:
    print('The cinema room is not full.')