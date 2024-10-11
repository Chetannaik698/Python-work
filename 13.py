def Cal_Sum(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

print(Cal_Sum(2,8))

def student_info(**details):
    for key,value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="Python")


def employee_data(**data):
    for key,value in data.items():
        print(f"{key}: {value}")
    
employee_data(name ="Chetan", salary=20000)

double = lambda n: n*2
print(double(4))

students = [
    {"name": "Chetan", "age": 19, "marks": 90},
    {"name": "Karan", "age": 19, "marks": 60},
    {"name": "Arun", "age": 19, "marks": 80},
]

students.sort(key=lambda x: x["marks"],reverse=True)
print(students)


def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)

print(fact(5))

def outer_func(name):
    def inner_func():
        print(f"Hello! {name}")
    inner_func()

outer_func("Chetan")

mul = lambda a,b: a*b
print(mul(2,3))

#sum of n numbers using rexursion

def return_sum(n):
    if n==1:
        return n
    return n + return_sum(n-1)

print(return_sum(5))

def return_avg(*numbers):
    avg = 0
    total = 0
    for num in numbers:
        total = total + num
        avg = (total/2)
    return avg

print(return_avg(2, 3, 5))