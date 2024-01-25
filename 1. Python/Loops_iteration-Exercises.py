# Loops and iteration - Exercises 1-2

print("""
      Exercise 1:
      """)

students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "RaphaÃ«l",
    "Axel",
    "Mathieu",
    "Adrien",
    ]

for list in students:
    print(list)

# Ex 2
    
print("""
      Exercise 2:
      """)
    
M_names = [item for item in students if item.startswith('M')]
print(M_names)

