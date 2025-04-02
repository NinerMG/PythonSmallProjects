# Errors, Exceptions and saving JSON data

# poprawa generatora haseł - wyszukiwanie haseł dla zapisanej strony


# proba otwarcia pliku który nie istnieje
# with open("a_file.txt") as file:
#     file.read()

#KeyError
# a_dictionary = {"key" : "value"}
# value = a_dictionary["non_existing_key"]

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)

# try
# coś co może powodować wyjątek
# except
# zrób to jeśli pojawił się wyjątek
# else:
# zrób to jeśli nie było wyjątków
# finally:
# zrób to nieważne co się stało

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key" : "value"}
#     value = a_dictionary["non_existing_key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Someting")
# except KeyError as error_message:
#     print(f"{error_message}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("The file was closed")


# definiowanie własnych błędow
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     value = a_dictionary["non_existing_key"]
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Someting")
# except KeyError as error_message:
#     print(f"{error_message}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError


# height = float(input("Height:"))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human height should not be over 3 meters")
#
# bmi = weight / height ** 2
# print(bmi)