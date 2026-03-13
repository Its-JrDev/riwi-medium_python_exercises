print('--Recreational Club: Membership Registration--')

# Plan prices
plan_prices = {
    'basic': 50000,
    'premium': 90000,
    'family': 130000
}

# Counters for each plan
count_basic = 0
count_premium = 0
count_family = 0

# Accumulator for total collected
total_collected = 0

while True:
    print('\nRegister a new member (or type "stop" to finish)')

    # Name input
    name = input('Enter member name: ').strip()
    if name.lower() == 'stop':
        break
    if not name:
        print('Error: name cannot be empty.')
        continue

    # Age input
    while True:
        try:
            age = int(input('Enter age: '))
            if age <= 0:
                print('Error: age must be positive.')
                continue
            break
        except ValueError:
            print('Error: enter a valid integer.')

    # Plan input
    while True:
        plan = input('Enter plan (basic/premium/family): ').lower()
        if plan in plan_prices:
            break
        print('Error: enter a valid plan.')

    # Display age-related messages
    if age < 18:
        print('Youth registration')
    elif age >= 60:
        print('Senior benefit')

    # Add to counters and total
    if plan == 'basic':
        count_basic += 1
    elif plan == 'premium':
        count_premium += 1
    else:
        count_family += 1

    total_collected += plan_prices[plan]

    print(f'Member {name} registered with plan {plan} (${plan_prices[plan]})')

# Final summary
print('\n----Summary----')
print(f'Total collected: ${total_collected}')
print(f'Number of basic plans: {count_basic}')
print(f'Number of premium plans: {count_premium}')
print(f'Number of family plans: {count_family}')

# Determine most sold plan
max_count = max(count_basic, count_premium, count_family)
if max_count == count_basic:
    print('Most sold plan: basic')
elif max_count == count_premium:
    print('Most sold plan: premium')
else:
    print('Most sold plan: family')