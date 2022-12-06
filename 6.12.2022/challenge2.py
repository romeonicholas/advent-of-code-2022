# Challenge 2 of 2 for 6.12.2022
# Input: A stream of a-z characters
# Goal: For the given stream, identify the position of the last character in the first occurance of 
# 14 unique characters in a row

challenge_input = open("input.txt", "r")
data = challenge_input.read()

slice_start = 0

while slice_start < len(data) - 14:
    sliced_section = data[slice_start:(slice_start + 14)]
    chars = set()

    for char in sliced_section:
        chars.add(char)

    if len(chars) == 14:
        break

    slice_start += 1

print(slice_start + 14)
