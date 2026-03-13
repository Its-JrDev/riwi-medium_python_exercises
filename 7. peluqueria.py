shifts = {
    'morning': range(6, 12),
    'afternoon': range(12, 18),
    'evening': range(18, 23),
    'outside hours': list(range(0, 6)) + list(range(23, 24))
}

print('Entry System for J. Style Hair Salon.')

while True:
    try:
        hour = int(input('Enter the client\'s arrival hour: '))
        if hour in shifts['morning']:
            print(f'The client arrived in the {list(shifts.keys())[0]}. The service price is $20,000 pesos.')
            break
        elif hour in shifts['afternoon']:
            print(f'The client arrived in the {list(shifts.keys())[1]}. The service price is $20,000 pesos.')
            break
        elif hour in shifts['evening']:
            print(f'The client arrived in the {list(shifts.keys())[2]}. The service price is $20,000 pesos.')
            break
        elif hour in shifts['outside hours']:
            print('The client arrived outside business hours. No service was provided.')
            break
        else:
            print('Error: The entered hour is not valid. Please enter an hour between 0 and 23.')
    except ValueError:
        print('Error: Please enter a valid number.')