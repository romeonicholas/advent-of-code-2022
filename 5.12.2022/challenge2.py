# Challenge 2 of 2 for 5.12.2022
# Input: A visual diagram of letters in brackets in numbered stacks,
# followed by a list of instructions where each line indicates the number
# of letters to be moved from one stack to another 
# Goal: Find out which letter will be on top of each stack after all moves
# if multiple crates can me moved at a time without changing their order

challenge_input = open("input.txt", "r")
data = challenge_input.read().splitlines()

crate_map = data[0:8]
crate_indices = data[8]
move_list = data[10:]

index_positions = []
index_count = 0

#Get number of stacks and the index associated with them
for char in crate_indices:
    if char.isnumeric():
        index_positions.append(index_count)
    index_count += 1

#Build correctly sized placeholder for stacks
crate_stacks = []
for positions in index_positions:
    crate_stacks.append([])

#Add all crates to their appropriate rows
for row in crate_map:
    for i in index_positions:
        if row[i].isalpha():
            crate_stacks[index_positions.index(i)].insert(0,row[i])

#Move crates based on move list
for move in move_list:
    move_values = [int(i) for i in move.split() if i.isdigit()]
    number_of_crates = move_values[0]
    start_position = move_values[1]
    end_position = move_values[2]

    crates_to_move = []
    i = 1
    while i <= number_of_crates:
        crates_to_move.append(crate_stacks[start_position - 1].pop())
        i += 1

    while crates_to_move != []:
        crate_stacks[end_position - 1].append(crates_to_move.pop())

topmost_crates = ""
for stack in crate_stacks:
    topmost_crates += stack.pop()

print(topmost_crates)