# Loops and iteration - Exercise 6

print("Exercise 6 :")

list = [17, 38, 10, 25, 72]
sorted_list = sorted(list)
print("Sorted list :", sorted_list)
list = list + [12]
print("List with 12 :", list)
list = list[::-1]
print("Reversed list :",list)
print("Index of element 17 :", list.index(17))
list.remove(38)
print("List without 38 :", list)
print("First two elments :", list[:2])
print("Three last elements :",list[-3:])
list = list[:2] + list[-3:]
print("Print the last two lists :", list)
print(list[-1:])






#print(list)