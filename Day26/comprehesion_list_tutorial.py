# list and dictonaries comprehesions
# jak stworzyć listy używając comprehesions - tworzenie nowej listy z poprzedniej listy
# new_list = [new_item for item in list]
numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
print(numbers)
print()
print(new_list)

name = "Angela"
new_list2 = [letter for letter in name]
print(new_list2)

new_list3 = [n for n in range(1,5)]
print(new_list3)

# można też dodawać warunki
# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) > 5]
print(short_names)