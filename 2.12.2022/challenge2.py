#Challenge 2 of 2 for 2.12.2022
#Goal: Calculate your score for a Rock, Paper, Scissors tournament
#Input: A text file with two columns of letters
#First coluimn is the opponent's move (Rock: A, Paper: B, Scissors: C)
#Second column is the round's outcome (Lose: X, Tie: Y, Win: Z)
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
    "C": "scissors"
}

OUTCOMES = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}

POINTS = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "lose": 0,
    "draw": 3,
    "win": 6
}

#desired outcome: opponent move: player move
REQUIRED_MOVES = {
    "lose": {"rock": "scissors", "paper": "rock", "scissors": "paper"},
    "draw": {"rock": "rock", "paper": "paper", "scissors": "scissors"},
    "win": {"rock": "paper", "paper": "scissors", "scissors": "rock"}
}

total_score = 0

for game in data:
    opponent_move = MOVES[game[0]]
    outcome = OUTCOMES[game[2]]
    player_move = REQUIRED_MOVES[outcome][opponent_move]

    total_score += POINTS[player_move]
    total_score += POINTS[outcome]

print(total_score)
