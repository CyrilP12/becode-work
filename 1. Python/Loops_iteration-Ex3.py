# Loops and iteration - Exercises 3-4

# Ecercise 3

print("""
      Exercise 3 :
      """)

for x in range(15):
    print(x)

print("""
      Exercise 4 :
      """)

for x in range(1, 11):
    print(x)
    if x == 5:
        break

print("""
      Exercise 4bis alias 5 :
      """)

for x in range(1, 11):
    print(x)
    if x >= 5:
        print("Interrupt at 5.")
        continue
    