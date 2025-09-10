def grades_from_user(): 
    grade_list = []
    ask_for_grades = True 
    while ask_for_grades:
        grade = int(input("Please enter next grade: "))
        if grade == -1: 
            ask_for_grades = False 
        elif grade >= 1 and grade <= 10: 
            grade_list.append(grade)
        else: 
            print("Please enter a grade between 1-10 (enter -1 to stop)")
    return grade_list

grade_list = grades_from_user()
print(grade_list)
print("You have entered: " + str(grade_list))

minimum_grade = grade_list[0]
for num in grade_list: 
    if num < minimum_grade: 
        minimum_grade = num
print("The minimum grade is: " + str(minimum_grade))

maximum_grade = grade_list[0]
for num in grade_list: 
    if num > maximum_grade: 
        maximum_grade = num
print("The maximum grade is: " + str(maximum_grade))


sum_of_grades = 0
for num in grade_list: 
    sum_of_grades += num 
total_grades = len(grade_list)
average = sum_of_grades / total_grades 
print("The grade average is: " + str(average))
