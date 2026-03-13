services = {
    1: 'Massage',
    2: 'Facial',
    3: 'Manicure'
}

print('Welcome to Unrated Sensations Spa.')

print('\nWe currently offer the following services:')

print('\n      ----Services Table----')
print(f'| {list(services.keys())[0]}.{services[1]} | {list(services.keys())[1]}.{services[2]} | {list(services.keys())[2]}.{services[3]} |')

while True:
    try:
        service_opt = int(input('\nChoose the number of your service: '))
        if service_opt in services.keys():
            print(f'\nCongratulations! You have chosen the {services[service_opt]} service.')
        else:
            print('Error: Please choose a valid option.')
            continue
        break
    except ValueError:
        print('\nError: Please enter an integer.')