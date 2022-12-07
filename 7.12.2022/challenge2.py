# Challenge 2 of 2 for 7.12.2022
# Input: A series of terminal commands and output separated by line breaks. Lines starting
# with $ are commands, integers are the size of the file on the same line, dir are directories
# that may contain additional files and directories inside
# Goal: Find the size of the smallest directory that, if deleted, would leave at least 30000000
# space available on the file system if its total available size is 70000000

challenge_input = open("input.txt", "r")
data = challenge_input.read().splitlines()

parent_directories = []
exited_directories = []
add_size_to_totals = False
i = 0

while i < len(data):
    if add_size_to_totals:
        split_line = data[i].split(" ")
        if split_line[0].isnumeric():
            j = 0
            while j < len(parent_directories):
                parent_directories[j]["size"] += int(split_line[0])
                j+=1
        elif split_line[0] == "$":
            add_size_to_totals = False

    if data[i] == "$ cd ..":
        exited_directories.append(parent_directories.pop())
    elif data[i][0:4] == "$ cd":
        if data[i][6:] not in parent_directories:
            if data[i][6:] not in exited_directories:
                parent_directories.append({
                    "name": data[i][5:],
                    "size": 0
                    })
            else:
                parent_directories.append(
                    exited_directories.pop(
                        exited_directories.index(data[i][5:])))
    elif data[i][0:4] == "$ ls":
        add_size_to_totals = True

    i += 1

all_directories = parent_directories + exited_directories
file_drive_space = 70000000
maximum_space_used = file_drive_space - 30000000

outer_most_directory_size = 0
for directory in all_directories:
    if directory["name"] == "/":
        outer_most_directory = directory

current_unused_space = file_drive_space - outer_most_directory["size"]
amount_of_space_required = 30000000 - current_unused_space

smallest_size_over_minimum = outer_most_directory["size"]
for directory in all_directories:
    if directory["size"] >= amount_of_space_required:
        if directory["size"] < smallest_size_over_minimum:
            smallest_size_over_minimum = directory["size"]

print(smallest_size_over_minimum)
