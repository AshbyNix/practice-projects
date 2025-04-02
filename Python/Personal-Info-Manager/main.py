# Personal Info Manager - collects and stores basic user information


first_name = input("First Name:> ")
last_name = input("Last Name:> ")
age = int(input("Age:> "))
height = int(input("Height(cm):> "))

age = age + 5

height = height / 100

print(f"\nHow are you today {first_name}, {last_name}")
print(f"\nIn five years you will be {age}")
print(f"\nYou are {height}m.")