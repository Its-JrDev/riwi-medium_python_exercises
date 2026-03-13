print('--Language Center: Student Evaluation--')

# Counters for levels
low_count = 0
medium_count = 0
high_count = 0

# Accumulators
total_average = 0
student_count = 0
best_student = None
best_average = 0

while True:
    print(f'\nStudent {student_count + 1}')

    # Name input
    name = input('Enter student name (or "stop" to finish): ').strip()
    if name.lower() == 'stop':
        break
    if not name:
        print('Error: name cannot be empty.')
        continue

    # Grades input
    while True:
        try:
            speaking = float(input('Enter speaking grade: '))
            listening = float(input('Enter listening grade: '))
            reading = float(input('Enter reading grade: '))
            if any(grade < 0 or grade > 100 for grade in (speaking, listening, reading)):
                print('Error: grades must be between 0 and 100.')
                continue
            break
        except ValueError:
            print('Error: enter valid numbers for grades.')

    # Calculate simple average
    avg = (speaking + listening + reading) / 3
    total_average += avg
    student_count += 1

    # Classify student
    if avg < 60:
        level = 'low'
        low_count += 1
    elif avg < 80:
        level = 'medium'
        medium_count += 1
    else:
        level = 'high'
        high_count += 1

    print(f'Student average: {avg:.2f} → Level: {level}')

    # Track best student
    if avg > best_average:
        best_average = avg
        best_student = name

# Final results
if student_count > 0:
    general_avg = total_average / student_count
    print('\n----Summary----')
    print(f'General average of the group: {general_avg:.2f}')
    print(f'Best student: {best_student} ({best_average:.2f})')
    print(f'Number of students in low level: {low_count}')
    print(f'Number of students in medium level: {medium_count}')
    print(f'Number of students in high level: {high_count}')
else:
    print('No students were registered.')