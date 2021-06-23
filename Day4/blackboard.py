from class_stats import blackboard_class, exam_weights
from blackboard_util import display_exam_grades, calculate_final_grade

menu = """ 
---------------
Professor's Menu 
---------------
0 - View Student ID
1 - Exam 1
2 - Exam 2
3 - Exam 3
4 - Calculate Final Grade
5 - Calculate ALL Final Grades
---------------
Enter your selection: 
""" 
user_selection = input(menu)

student_name = input("Which student's grades would you like to see? ")
student_name = student_name.lower()

try: 
    temp = blackboard_class[student_name]
except: 
    print("Student does not exist.")
    raise 



if user_selection == "0":
    print(f"{student_name.title()} ID : {blackboard_class[student_name]['id']}")
elif user_selection == "1" or user_selection == "2" or user_selection == "3":
    display_exam_grades(blackboard_class, student_name, user_selection)
elif user_selection == "4":
    calculate_final_grade(blackboard_class, student_name) 
elif user_selection == "5":
    for name in blackboard_class.keys():
        calculate_final_grade(blackboard_class, name)
else:
    print("Invalid Selection. Please try again.")





