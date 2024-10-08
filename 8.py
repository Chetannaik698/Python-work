# time = input("Enter time: ")

# if time == "8AM":
#     print("It's time to Breakfast")
# elif time == "1PM":
#     print("It's time for lunch")
# elif time == "8PM":
#     print("It's time for Dinner")
# else:
#     print("It's not meal time.")

item = input("Enter the item name: ")

if item == "Sugar":
    KG = int(input("Enter how much KG you want: "))
    if KG > 4:
        print("You get discount of 20 rupees")
    else:
        print("You have to pay amount as per KG")
elif item == "Rice":
    bag = int(input("Enter number of bag you want purchase: "))
    if bag > 2:
        print("You get discount of 100 rupees for each bag")
    else: 
        print("You have to pay full amount")
else:
    print("Your item is not in our shop")