# Working with files and directories
# ulepszenie gry snake - śledzenie high score

#file = open("my_file.txt")
#contents = file.read()
#print(contents)
#file.close()


#with open("my_file.txt") as file_two:
#    text = file_two.read()
#    print(text)

#with open("my_file.txt", mode="w") as file:
#    file.write("New line of text.")
#with open("my_file.txt", mode="a") as file:
#    file.write("\nNew line of text.")

with open("my_file2.txt", mode="a") as file:
    file.write("\nNew line of text.")


#teraz w snake można dodać plik txt przechowujący highscore