# Challenge 1 of 2 for 6.12.2022
# Input: A stream of a-z characters
# Goal: For the given stream, identify the position of the last character in the first occurance of 
# 4 unique characters in a row (e.g. aaabcdaaa <- position 6)

challenge_input = open("input.txt", "r")
data = challenge_input.read()

slice_start = 0

while slice_start < len(data) - 4:
    chars = {
        data[slice_start],
        data[slice_start + 1],
        data[slice_start + 2],
        data[slice_start + 3],
    }

    if len(chars) == 4:
        break

    slice_start += 1

print(slice_start + 3 + 1) #list is 0-inexed, but answer needs to be 1-indexed
