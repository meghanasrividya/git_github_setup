# What is a Dictionary?
# How to manage data using Dictionaries
# How does it work as key= value
# Syntax { "name": "Sparta"}

# store student's data-name,course_name,progress,completed_lessons

student_1 = {
    "keys":"values",
    "name": "Meghana",
    "stream":"DevOps",
    "completed_lessons":4,
    "completed _lessons_names":["lists","tuples","strings"]
}
print(student_1)
print(type(student_1))
print(student_1["stream"])# This will display the value saved inside stream
#print/display completed_lessons_names
print(student_1["completed _lessons_names"])
#print/display completed_lessons_names index 0 means lists
print(student_1["completed _lessons_names"][0])# displays lists
print(student_1["completed _lessons_names"][1])# displays tuples
print(student_1["completed _lessons_names"][2])# displays strings