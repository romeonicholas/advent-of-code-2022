# Challenge 1 of 2 for 3.12.2022
# Input: A list of newline separate strings consisting of only a-zA-Z
# Goal: Identify which letter is present in both the first half and second half
# of each line and add its value (1-26 for a-z, 27-52 for A-Z) to a running total.
# Each line is even (can be split down the middle), and only one letter will
# appear in both the first and second half, but multiples of that character may
# be present. Get the sum of the value types, not of the number of those characters.

challenge_input = open("input.txt", "r")
data = challenge_input.read().splitlines()

priorities = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "U": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52,
}
sum_of_priorities = 0

for line in data:
    rucksack_1 = line[: int(len(line) / 2)]
    rucksack_2 = line[int(len(line) / 2) :]

    for item in rucksack_1:
        if item in rucksack_2:
            sum_of_priorities += priorities[item]
            break

print(sum_of_priorities)
