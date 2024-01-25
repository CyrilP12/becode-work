# Loops and iteration - While

i = 1

while i <= 10:
    print(i)
    i += 1

while True:
    n = int(input("give a integer > 0 : "))
    print("You have provided", n)
    if n > 0:
        break
print("correct answer")