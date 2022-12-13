from dotenv import load_dotenv
from aocd import get_data,submit

load_dotenv()
YEAR=2022
DAY=2

# A,X = Stone = 1
# B,Y = Paper = 2
# C,Z = Scissor = 3

OUTCOME_A = {
    "B X": 0+1,
    "C Y": 0+2, 
    "A Z": 0+3, 
    "A X": 3+1, 
    "B Y": 3+2, 
    "C Z": 3+3, 
    "C X": 6+1, 
    "A Y": 6+2, 
    "B Z": 6+3, 
}

# X = Lose = 0
# Y = Draw = 3
# Z = Win = 6

OUTCOME_B = {
    "B X": 0+1,
    "C X": 0+2, 
    "A X": 0+3, 
    "A Y": 3+1, 
    "B Y": 3+2, 
    "C Y": 3+3, 
    "C Z": 6+1, 
    "A Z": 6+2, 
    "B Z": 6+3, 
}


def calculate_game_result(data:str,outcome:dict):
    game_total_points = 0
    for round in data.splitlines():
        game_total_points += outcome[round]
    return game_total_points


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR)

    game_result_a = calculate_game_result(data,OUTCOME_A)
    assert(game_result_a==12535)
    submit(game_result_a,"a",day=DAY,year=YEAR)

    game_result_b = calculate_game_result(data,OUTCOME_B)
    assert(game_result_b==15457)
    submit(game_result_b,"b",day=DAY,year=YEAR)
