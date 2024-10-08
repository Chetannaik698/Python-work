students = ["Chetan", "karan", "Vinod", "Abay"]
marks = [20, 30, 40, 90]

Final_dict = {}

for idx, student in enumerate(students):
    Final_dict[student] = marks[idx]
print(Final_dict)

workers = {
    "Mahesh": 20000,
    "Suresh": 20000,
    "Ganesh": 32000,
    "Karan": 43000,
}

for name,salary in workers.items():
    print(f"{name}'s salary is {salary}")

numbers = [2, 4, 6, 8, 12, 14, 6, 18]
new_list = [num**2 for num in numbers if num % 2 == 0] # at first here num symbolises the rxpression
print(new_list)

cities = ["Banglore", "manglore", "Hubbali", "Delhi", "Hydrabad"]
large_cities = [city for city in cities if len(city) > 7]
print(large_cities) 

new_dict = {name: salary for name, salary in workers.items()}
print(new_dict)