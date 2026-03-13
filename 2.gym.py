print('Welcome to J. Sports Gym.')
print('\nWe currently offer the following classes according to age group: ')
print('- Youth classes (13-17 years)')
print('- General classes (18-59 years)')
print('- Senior classes (60+ years)')

while True:
    try:
        age = int(input('\nPlease enter your age to see which class you can attend: '))
        if age in range(13, 18):
            print('You can attend the youth classes.')
        elif age in range(18, 60):
            print('You can attend the general classes.')
        elif age >= 60:
            print('You can attend the senior classes.')
        else:
            print('Sorry, you cannot attend our classes. You must be at least 13 years old.')
        break
    except ValueError:
        print('Error: Please enter a valid number.')