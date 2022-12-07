# Challenge 1 of 2 for 7.12.2022
# Input: A series of terminal commands and output separated by line breaks. Lines starting
# with $ are commands, integers are the size of the file on the same line, dir are directories
# that may contain additional files and directories inside
# Goal: Find all directories with a total size of less than or equal to 100,000 and sum them,
# noting that this size CAN count files multiple times (once for each directory or 
# subdirectory included)

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

total_sums_of_under_100000 = 0
all_directories = parent_directories + exited_directories

for directory in all_directories:
    if directory["size"] <= 100000:
        total_sums_of_under_100000 += directory["size"]

print(total_sums_of_under_100000)
