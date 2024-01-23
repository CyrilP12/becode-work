# Basics operators ex 8

bottle_milk = 0.45
bottle_cider = 3.85
bag_flour = 0.9
packet_butter = 0.77
jar_nutella = 1.87
orderPrice = (2*bottle_milk) + (3*bottle_cider) + bag_flour + packet_butter + jar_nutella
#orderPrice = 23
allowanceMoney = 20
allowanceMoney -= orderPrice

if allowanceMoney > 0:
    print("You have spent", orderPrice, "you have left", allowanceMoney)
elif allowanceMoney < 0:
    print("Sorry you're missing", allowanceMoney, "euros")
elif allowanceMoney == 0:
    print("You are broke!")