# Loops and iteration - Exercise 8
# The price is right!

number_to_find = 42

user_number = int(input("Enter a number : "))

while user_number != number_to_find:
    if user_number > number_to_find:
        print("It's less.")
        user_number = int(input("Wrong number, plese enter an other one : "))
    elif user_number < number_to_find:
        print("It's more.")
        user_number = int(input("Wrong number, plese enter an other one : "))
print("Well done, you won!")

