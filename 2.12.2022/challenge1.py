#Challenge 1 of 2 for 2.12.2022
#Goal: Calculate your score for a Rock, Paper, Scissors tournament
#Input: A text file with two columns of letters
#First coluimn is the opponent's move (Rock: A, Paper: B, Scissors: C)
#Second column is your move (Rock: X, Paper: Y, Scissors: Z)
#The score for each round is calculated as follows:
#Played Rock: +1 point
#Played Paper: +2 points
#Played Scissors: +3 points
#Lost: +0 points
#Tied: +3 points
#Won: +6 points

challenge_input = open("input.txt", "r")
data = challenge_input.read().splitlines()

MOVES = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

POINTS = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lose": 0,
    "draw": 3,
    "win": 6
}

#opponent move: player move: outcome
OUTCOMES = {
    "rock": {"rock": "draw", "paper": "win", "scissors": "lose"},
    "paper": {"rock": "lose", "paper": "draw", "scissors": "win"},
    "scissors": {"rock": "win", "paper": "lose", "scissors": "draw"}
}

total_score = 0

for game in data:
    opponent_move = MOVES[game[0]]
    player_move = MOVES[game[2]]

    total_score += POINTS[player_move]
    total_score += POINTS[OUTCOMES[opponent_move][player_move]]

print(total_score)
