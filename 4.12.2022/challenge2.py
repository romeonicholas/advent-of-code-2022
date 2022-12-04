# Challenge 2 of 2 for 4.12.2022
# Input: A list of pairs of ranges, with range pairs on the same line separated by commas
# Goal: Count how many of the range pairs overlap at all

challenge_input = open("input.txt", "r")
data = challenge_input.read().splitlines()

count_of_overlapping_ranges = 0

for range_pairs in data:
    ranges = range_pairs.split(",")
    range_1 = ranges[0]
    range_2 = ranges[1]

    boundaries_1 = range_1.split("-")
    lower_boundary_1 = int(boundaries_1[0])
    upper_boundary_1 = int(boundaries_1[1])

    boundaries_2 = range_2.split("-")
    lower_boundary_2 = int(boundaries_2[0])
    upper_boundary_2 = int(boundaries_2[1])

    if (
        (lower_boundary_1 >= lower_boundary_2 and lower_boundary_1 <= upper_boundary_2) or
        (upper_boundary_1 <= upper_boundary_2 and upper_boundary_1 >= upper_boundary_2) or
        (lower_boundary_2 >= lower_boundary_1 and lower_boundary_2 <= upper_boundary_1) or
        (upper_boundary_2 <= upper_boundary_1 and upper_boundary_2 >= upper_boundary_1)
    ):
        count_of_overlapping_ranges += 1

print(count_of_overlapping_ranges)
