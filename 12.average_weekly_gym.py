clients = 5
count_low = 0
count_med = 0
count_high = 0

def weekly_assists():
    try:
        assists = int(input('Number of days attended in the week: '))
        if assists < 0:
            print('Error: Negative numbers are not allowed.')
            return weekly_assists()
        return assists
    except ValueError:
        print('Error: Please enter an integer.')
        return weekly_assists()

def daily_avg_minutes():
    try:
        minutes = int(input('Average minutes trained per day: '))
        if minutes < 0:
            print('Error: Negative numbers are not allowed.')
            return daily_avg_minutes()
        return minutes
    except ValueError:
        print('Error: Please enter an integer.')
        return daily_avg_minutes()

for i in range(clients):
    print('\nWelcome to J. Sports Gym.')
    name = input('\nEnter your name: ').strip().lower().capitalize()
    assisted_times = weekly_assists()
    minutes_trained = daily_avg_minutes()
    
    if assisted_times in range(0, 3):
        print('\nYou show a low commitment to attendance.')
        count_low += 1
    elif assisted_times in range(3, 5):
        print('\nYou show a medium commitment to attendance.')
        count_med += 1
    elif assisted_times >= 5:
        print('\nYou show a high commitment to attendance.')    
        count_high += 1
        
print('\n----Commitment Classification----')
print(f'People with high commitment: {count_high}')
print(f'People with medium commitment: {count_med}')
print(f'People with low commitment: {count_low}')