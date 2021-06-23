exam1_grades = {
    "bob" : 23,
    "patrick" : 55,
    "james" : 100
}

# print(exam1_grades.keys())
# print(exam1_grades.values())
# print(exam1_grades["bob"])

# print(exam1_grades[23]) 
# ^ this will not work, you can only use keys to access values, 
# you can not use values to access keys 

name = "kelvin"
print(name in exam1_grades)
# print("kelvin" in exam1_grades.keys())