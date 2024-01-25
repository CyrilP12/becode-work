# Loops and iteration - Continue and Break
# Continue

for i in range(4):
    print("Start of iteration", i)
    print("Hello")
    if i < 2:
        continue
    print("End of iteration", i)
print("After the loop")

#Break
print("""
      Beginning Break :
    """)

for i in range(10):
    print("Start of iteration", i)
    print("Hello")
    if i == 2:
        break
    print("End of iteration", i)
print("After the loop")