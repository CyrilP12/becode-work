# Loops and iteration - Exercise 10

    
languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]

for i, lang_group in enumerate(languages):
    for lang in lang_group:
        if i == 0:
            print(f"{lang} is a backend language?")
        elif i == 1:
            print(f"{lang} is a frontend language?")
