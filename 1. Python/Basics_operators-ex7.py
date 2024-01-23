# Basics operators ex
age = int(input("write a number :"))
age += 10
divAge = int(age // 7)
textDiv = "{} divided by 7 equals {}" .format(age, divAge)
restDiv = int(divAge%7)
expDiv = restDiv ** 3
print(expDiv)
