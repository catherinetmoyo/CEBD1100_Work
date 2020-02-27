with open("my_input_file.txt") as file_object:
    contents = file_object.read()

    print(contents.rstrip())


# with open("my_input_file.txt") as f:
    # for line in f:
        # print(line.rstrip())



with open("my_input_file.txt") as f:
    lines = f.readlines()

for l in lines:
    print(l)

print(len(lines))



