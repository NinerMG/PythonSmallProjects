# jak wygląda struktura plików, czym się różni relative i absolute path
# projekt -> zamiana jednego słowa w plliku txt i zapisanie go jako nowy
# file readlines()
# metoda replace()
# metoda strip()

PLACEHOLDER = "[name]"

with open("invited_names.txt") as names_file:
    names = names_file.readlines()
    #print(names)

with open("starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        #print(new_letter)
        with open(f"./output/letter_for{stripped_name}.txt", mode="w") as competed_letter:
            competed_letter.write(new_letter)
