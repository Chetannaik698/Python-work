def table(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
    
table(2)

def func(n):
    return n * n

a = 100
b = func(2)
c = a + b

print(c)

def greet(name):
    print(f"Hello {name} Welcome!")

greet("Chetan")
greet("Akshay")

def sum(a,b):
    return a + b

c = sum(2,4)
print(c)