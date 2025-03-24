
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76,98]
}

# looping through dictionaries:
for (key, value) in student_dict.items():
    print(value)

import pandas

student_data_frame =  pandas.DataFrame(student_dict)
# print(student_data_frame)

# loop through data frame
# for (key, value) in student_data_frame.items()
#     print(value)

# pandas ma sposób na iterowanie
# loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    #print(index)
    print(row.score)