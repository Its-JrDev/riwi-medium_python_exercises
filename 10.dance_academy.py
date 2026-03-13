assists = {
    'low' : range(0, 5),
    'medium' : range(5, 9),
    'high' : 9
}

print('----Attendance Management System for J. Dance & Co----')

while True:
    try:
        attendance_count = int(input('\nEnter the number of student attendances: '))
        if attendance_count < 0:
            print('\nError: Attendance count cannot be negative.')
        else:
            break
    except ValueError:
        print('\nError: Please enter an integer.')

if attendance_count in assists['low']:
    print(f'\nThe student has a {list(assists.keys())[0]} attendance record.')
elif attendance_count in assists['medium']:
    print(f'\nThe student has a {list(assists.keys())[1]} attendance record.')
elif attendance_count >= assists['high']:
    print(f'\nThe student has a {list(assists.keys())[2]} attendance record.')