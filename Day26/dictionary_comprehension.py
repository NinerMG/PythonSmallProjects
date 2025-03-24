# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.item()}
# new_dict = {new_key:new_value for (key,value) in dict.item() if test}
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
students_score = {student:random.randint(1,100) for student in names}
print(students_score)