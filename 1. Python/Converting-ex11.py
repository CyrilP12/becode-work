# Converting
dollar = 1.09
euro = 0.92
currency = input("Write E for euro or $ for dollar for the amount you want to convert :")

if currency == "E" :
    amount = int(input("Write amount : "))
    print(dollar*amount)
elif currency == "$" :
    amount = int(input("Write amount : "))
    print(euro*amount)
else :
    currency = input("Please enter the correct currency beetween E or $ : ")



