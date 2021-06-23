def display_exam_grades(class_dict, name, exam_number):
    exam_key = f"exam{exam_number}"

    print("\n")
    print('-' * 30)
    print(f"{name.title()} exam {exam_number} grade:")

    exam_questions = class_dict[name][exam_key].keys()
    exam_total = sum(class_dict[name][exam_key].values())

    print('-' * 30)
    for question in exam_questions:
        question_grade = class_dict[name][exam_key][question]
        print(f"Exam {exam_number} {question} : {question_grade}")
    print('-' * 30)
    print(f"Exam {exam_number} Total Grade : {exam_total}")


def calculate_final_grade(class_dict, name):
    student_stats = class_dict[name]
    exam_totals = []

    print("\n")
    print('-' * 30)
    for key in student_stats.keys():
        if "exam" in key: 
            exam_final_grade = sum(student_stats[key].values())
            exam_totals.append(exam_final_grade)
            print(f"Exam # {key[-1]} Grade : {exam_final_grade}")

    final_grade = sum(exam_totals)/len(exam_totals)
    print(f"\tFinal Grade for {name.title()} : {final_grade}")
    print('-' * 30)

            
