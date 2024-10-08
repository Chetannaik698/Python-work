# for loop
# students = ["Arun", "Abhishek", "vijay"]

# for student in students:
#     print(student, end= " ")

# for i in range(1,11,2):
#     print(i, end=" ")

name = "Chetan"

for idx, letter in enumerate(name):
    # print((idx + 1) * letter)
    print(f"{letter} is in {idx}th index")

data = {
    "name": "Chetan",
    "age": 19,
    "City": "Murudeshwar"
}

# print(data.items())

for key in data.items():
    print(key)


for i in range(2,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")