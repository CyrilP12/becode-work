# Drill functions - Exercises

#Exercise 1 - Hello name

print("""
      Exercise 1 :
      """)

def hello(name="Anonymous"):
    print(f"Hello {name}")
    return

hello('Jean')
hello()

#Exercise 2 - Count students

print("""
      Exercise 2 :
      """)

def sum_of_students(students):
        num_students = sum(len(sublist) for sublist in students)
        print(num_students)
        return 0

sum_of_students([["Jean", "Alice", "Edwige", "Peter", "James"],
               ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]])


# Exercise 3 - Is divisible ?

print("""
      Exercise 3 :
      """)

def is_divisible(n, x, y):
    # Your code
    n = str(input("Enter a number to divide : "))
    x = str(input("Enter the first divider : "))
    y = str(input("Enter the second divider : "))
    return n % x == 0 and n % y == 0

is_divisible()

# Exercise 4 - Abbreviation a two-word name

print("""
      Exercise 4 :
      """)

def abbreviate_name(name):
    parts = name.split(' ')
    initiales = [part[0].upper() for part in parts]
    return '.'.join(initiales)

name = input("name:")
abbreviate_name(name)
print(abbreviate_name(name))

# Exercise 5 - Sum of positive

print("""
      Exercise 5 :
      """)

def positive_sum(numbers= [1, -4, 7, 12]):
    positive_numbers = list(filter(lambda x: x > 0, numbers))
    print(positive_numbers)
    return 0

positive_sum()

# Exercise 6 - Sum mixed array



