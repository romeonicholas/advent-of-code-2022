#Challenge 2 of 2 for 1.12.2022
#Goal: Find the 3 Elves carrying the most Calories. How many total Calories are they carrying?
#Input: Integers represent the calories for each meal, meals carried by an elf are separated by newlines, and the elves are separated by a blank line

challenge_input = open("input2.txt", "r")
data = challenge_input.read().splitlines()

calories_by_elf = [0]
current_elf = 0

for meal in data:
    if meal != '':
        calories_by_elf[current_elf] += int(meal)
    else:
        calories_by_elf.append(0)
        current_elf += 1

calories_by_elf.sort()
sum_of_top_3_elves_calories = calories_by_elf[-1] + calories_by_elf[-2] + calories_by_elf[-3]

print (sum_of_top_3_elves_calories)
