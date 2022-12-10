# Challenge 1 of 2 for 10.12.2022
# Input: A series of line separated instructions: noop and addx value. X is
# the value being modified throughout, and starts at 1. The noop command
# takes a single cycle, and does not impact the value of x. The addx command
# takes two cycles, and at the END of the second cycle adds its value to x.
# Goal: If signal strength is represented by cycle number times the value of
# x DURING that cycle (not the end of it), find the summed cycle strength
# of cycles 20, 60, 100, 140, 180, and 220

challenge_input = open("input.txt", "r")
instructions = challenge_input.read().splitlines()

cycle = 1
x = 1
signal_strengths = []


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
        signal_strengths.append(cycle * x)
        if command == "addx":
            if cycle_duration == 1:
                x += value
            else:
                print("Waiting to add next cycle")

        cycle_duration -= 1
        cycle += 1

sum_of_signal_strengths = signal_strengths[19] + signal_strengths[59] + signal_strengths[99] + signal_strengths[139] + signal_strengths[179] + signal_strengths[219]
print(sum_of_signal_strengths)