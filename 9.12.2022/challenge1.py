# Challenge 1 of 2 for 9.12.2022
# Input: A series of line separated directions that consist if a (4-way) direction
# and the number of steps taken in that direction before changing direciton,
# separated by a space
# Goal: Using the directions from the input, simulate the path an object would take.
# Sum the number of unique spaces that would be visited by a connected object, that must
# always be touching the first object (one above/below/left/right, or diagonal) and
# that always takes the shortest path to follow the original object

challenge_input = open("input.txt", "r")
instructions = challenge_input.read().splitlines()

visited_positions = set()
head_col = 0
head_row = 0
tail_col = 0
tail_row = 0

for instruction in instructions:
    direction_and_steps = instruction.split(" ")
    direction = direction_and_steps[0]
    steps = int(direction_and_steps[1])

    while steps > 0:
        if direction == "R":
            if head_col > tail_col:
                tail_col += 1
                if head_row > tail_row:
                    tail_row += 1
                elif head_row < tail_row:
                    tail_row -= 1

            head_col += 1

        elif direction == "L":
            if head_col < tail_col:
                tail_col -= 1
                if head_row > tail_row:
                    tail_row += 1
                elif head_row < tail_row:
                    tail_row -= 1

            head_col -= 1

        elif direction == "D":
            if head_row > tail_row:
                tail_row += 1
                if head_col > tail_col:
                    tail_col += 1
                elif head_col < tail_col:
                    tail_col -= 1

            head_row += 1

        elif direction == "U":
            if head_row < tail_row:
                tail_row -= 1
                if head_col > tail_col:
                    tail_col += 1
                elif head_col < tail_col:
                    tail_col -= 1

            head_row -= 1

        visited_positions.add((tail_row,tail_col))

        steps -= 1

number_of_visited_positions = len(visited_positions)

print(number_of_visited_positions)
