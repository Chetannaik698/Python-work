age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult!")
elif age < 18:
    print("You are minor!")

str = input("Enter any string: ")
item = input("Enter character that you want to check exisistance: ")

if item in str:
    print(True)
else:
    print(False)

a = int(input("Enter value of a: "))
b = int(input("Enter the value of b: "))

print(a & b)
print(a | b)
print(a ^ b)
print(a >> b)
print(a << b)