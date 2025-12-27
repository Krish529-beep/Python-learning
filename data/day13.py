""" 
Student mark analyzer
"""

def collect_student_data():
    students = {}

    while 1:
        name = input('Enter the student name or done to close:').strip()
        
        if name.lower() == "done":
            break;
        if name in students:
            print('Student alredy exists')
            continue

        try:
            marks = float(input(f'Enter marks for {name}:'))
            students[name] = marks
        except ValueError:
            print('Pls enter a valid number for marks')

    return students

def display_report(students):
    if not students:
        print('no students data')
        return

    marks =  list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    avg_score = sum(marks) / len(marks)

    topper = [name for name,score in students.items() if max_score == score]
    bottomer = [name for name,score in students.items() if min_score == score]

    print('\n Students marks report')
    print('-'*30)
    print(f'total students {len(students)}')
    print(f'avg students {avg_score:.2f}')
    print(f'Highest students : {max_score:.2f} by {','.join(topper)}')
    print(f'Highest students : {min_score:.2f} by {','.join(bottomer)}')

    print('-' * 30)
    print('Detailed marks')
    for name,score in students.items():
        print(f'- {name} : {score}')


students= collect_student_data()
display_report(students)