import random
name = ['Lupe', 'Mark', 'Amber', 'Todd', 'Anita', 'Sandy']

new_dict = {
    student: random.randint(1,100) for student in name
}

passed_students = {student : score for (student, score) in new_dict.items() if score>60}
print(passed_students)