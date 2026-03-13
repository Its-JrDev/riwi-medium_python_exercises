rates = {
    "Children": 8000,
    "Adults": 12000,
    "Seniors": 9000
}

print('Welcome to the Cinema. We have the following rates: ')

print(f'- {list(rates.keys())[0]} (0-11 years): ${rates["Children"]:,} pesos')
print(f'- {list(rates.keys())[1]} (12-59 years): ${rates["Adults"]:,} pesos')
print(f'- {list(rates.keys())[2]} (60+ years): ${rates["Seniors"]:,} pesos')

while True:
    try:
        age = int(input('\nPlease enter your age to determine the ticket price: '))
        if age in range(0, 12):
            print(f'The ticket price for children is ${rates["Children"]:,} pesos.')
        elif age in range(12, 60):
            print(f'The ticket price for adults is ${rates["Adults"]:,} pesos.')
        elif age >= 60:
            print(f'The ticket price for seniors is ${rates["Seniors"]:,} pesos.')
        else:
            print('Error: We cannot process your request. Age must be a positive number.')
        break
    except ValueError:
        print('Error: Please enter a valid number.')