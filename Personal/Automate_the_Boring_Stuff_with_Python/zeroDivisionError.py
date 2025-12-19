def calculate_grade_average(grade_sum, number_of_grades):
    grade_average = int(grade_sum / number_of_grades)
    return grade_average

counter = 0
total = 0
while True:
    print('Enter a grade, or "done" if done entering grades:')
    grade = input()
    if grade == 'done':
        if counter == 0:
            print("No grades entered.")
            exit()
        break
    counter = counter + 1
    total = total + int(grade)

avg = calculate_grade_average(total, counter)
print('The grade average is:', avg)