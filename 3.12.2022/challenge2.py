# Challenge 2 of 2 for 3.12.2022
# Input: A list of newline separate strings consisting of only a-zA-Z
# Goal: Identify which letter is present in every 3 line grouping and add its
# value (1-26 for a-z, 27-52 for A-Z) to a running total. Only one letter will
# appear in all three lines, and that value only needs to be added once per group
# to the running total.


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

line = 0
while line < len(data):
    elf_1 = data[line]
    elf_2 = data[line + 1]
    elf_3 = data[line + 2]

    for item in elf_1:
        if item in elf_2:
            if item in elf_3:
                sum_of_priorities += priorities[item]
                break

    line += 3

print(sum_of_priorities)
