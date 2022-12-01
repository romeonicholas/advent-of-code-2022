#Challenge 1 of 2 for 1.12.2022
#Goal: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
#Input: Integers represent the calories for each meal, meals carried by an elf are separated by newlines, and the elves are separated by a blank line

challenge_input = open("input1.txt", "r")
data = challenge_input.read().splitlines()

meals_by_elf = [[]]
current_elf = meals_by_elf[0]
greatest_calorie_count = 0
current_calorie_count = 0

for meal in data:
    if meal != '':
        current_elf.append(meal)
        current_calorie_count += int(meal)
    else:
        meals_by_elf.append([])
        current_elf = meals_by_elf[-1]

        if current_calorie_count > greatest_calorie_count:
            greatest_calorie_count = current_calorie_count

        current_calorie_count = 0

print(greatest_calorie_count)
