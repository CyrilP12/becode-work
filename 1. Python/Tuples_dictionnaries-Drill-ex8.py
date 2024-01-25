# Tuples and dictionnaries - Drill exercises 8-9-10

articles_prices = {'Laser sword' : 229.0, 'Mitendo DX' : 127.30, 'Linux cushion' : 74.50, 'Goldorak briefs' : 29.90, 'Nextpresso' : 184.60}

values_prices = articles_prices.values()

sum_prices = sum(articles_prices.values())
print("Total price :", sum_prices)

removed_article = input("Enter an article to remove : ")

del articles_prices[removed_article]

print("Sum with removed article : ",sum(articles_prices.values()))



