# Challenge 1 of 2 for 10.12.2022
# Input: A series of line separated instructions: noop and addx value. X is
# the value being modified throughout, and starts at 1. The noop command
# takes a single cycle, and does not impact the value of x. The addx command
# takes two cycles, and at the END of the second cycle adds its value to x.
# Goal: Every cycle represents a draw call for that pixel position on a
# 40 wide by 6 high display, and will light up that pixel if x is within 1 of
# that cycle's pixel DURING the cycle. Draw the result of the input on the display.


challenge_input = open("input.txt", "r")
instructions = challenge_input.read().splitlines()

cycle = 1
x = 1
display_line = ""

for instruction in instructions:
    command_and_value = instruction.split(" ")
    command = command_and_value[0]
    value = 0
    if len(command_and_value) == 2:
        value = int(command_and_value[1])
    cycle_duration = 0
    
    if command == "noop":
        cycle_duration = 1
    elif command == "addx":
        cycle_duration = 2

    while cycle_duration > 0:
        if len(display_line) > 39:
            print(display_line)
            display_line = ""
            cycle -= 40

        if cycle == x or cycle == x+1 or cycle == x+2:
            display_line += "#"
        else:
            display_line += "."

        if command == "addx":
            if cycle_duration == 1:
                x += value
        

        cycle_duration -= 1
        cycle += 1

print(display_line)