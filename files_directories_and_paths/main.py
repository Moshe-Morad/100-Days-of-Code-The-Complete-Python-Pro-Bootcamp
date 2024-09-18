with open("my_file.txt") as read_file:
    contents = read_file.read()
    print(contents)

                       # mode="a"
with open("my_file.txt", mode="w") as write_file:
    contents = write_file.write("something")
