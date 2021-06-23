exam_grades = {
    "George": [100, 90, 95],
    "Cindy" : [90, 100, 90],
    "Bob": [80, 65, 85],
    "John" : [10, 15, 27],
    "Sarah": [95, 100, 100],
    "Patrick": [10, 40, 90]
}

# all midterms = 33.3% 
# final grade = mean of all exam grades 

for key in exam_grades.keys():
    print(f"Final grade for {key}: {sum(exam_grades[key]) / len(exam_grades[key])}")


