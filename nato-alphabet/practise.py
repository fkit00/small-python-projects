# list comprehension - making a list from a previous list 
import random 

numbers = [1,2,3,4]
new_numbers = [item+1 for item in numbers]
print(new_numbers)

name = "Fiona"
new_name=[print(letter) for letter in name]

new_list=[print(n*2) for n in range (0,6) if n%2==0]

names= ["a","b","c","d"]

student_score=  {student:random.randint(1,100) for student in names}

print(student_score)

passed_students= {key:value for (key,value) in student_score.items() if value > 60}
print(passed_students)