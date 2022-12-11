from dotenv import load_dotenv
from aocd import get_data,submit

from utility.decorators import timeit

load_dotenv()
YEAR=2022
DAY=1

@timeit
def compute_max_calories(data: str):
    idx0,idx1,max_calories = 0,0,0
    while idx1 < len(data):
        if not data[idx1]:
            calories = sum((int(i) for i in data[idx0:idx1]))
            if calories > max_calories:
                max_calories=calories
            idx0 = idx1+1
        idx1 += 1
    return max_calories

@timeit
def compute_top3_calories(data: str):
    idx0,idx1,calories = 0,0,[]
    while idx1 < len(data):
        if not data[idx1]:
            calories.append(sum((int(i) for i in data[idx0:idx1]))) 
            idx0 = idx1+1
        idx1 += 1
    calories.sort(reverse=True)
    return sum(calories[:3])


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR)

    max_calories = compute_max_calories(data.splitlines())
    assert(max_calories==70613)
    top3_calories = compute_top3_calories(data.splitlines())
    assert(top3_calories==205805)

    submit(max_calories,part="a",day=DAY,year=YEAR)
    submit(top3_calories,part="b",day=DAY,year=YEAR)
