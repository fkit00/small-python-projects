# list comprehension - making a list from a previous list 

numbers = [1,2,3,4]
new_numbers = [item+1 for item in numbers]
print(new_numbers)

name = "Fiona"
new_name=[print(letter) for letter in name]

new_list=[print(n*2) for n in range (0,6)]