# while loop

# Guessing Game
num = 20

while True:
    guess = 1
    while guess <= 3:
        user_guess = int(input(f" guesss {guess} | Guess the number: "))
        if num == user_guess:
            print("Congrats Correct guess!")
            break
        else:
            print("incorrect guess")
        guess = guess + 1
    if guess > 3:
        print(f"You lost your all three guess the correct num is {num}")
        break
    break

student = ["Chetan", "Karan", "Vijay", "Chandan", "Arun"]

i=0 

while i<len(student):
    print(student[i])
    i = i + 1

#printing table

table = int(input("Enter the table that you want to print: "))
i=1
while i<=10:
    print(f"{table} * {i} = ", table * i)
    i = i + 1

