from dotenv import load_dotenv
from aocd import get_data,submit

load_dotenv()
YEAR=2022
DAY=3


def calculate_total_item_points(data:str):
    total_points = 0
    for backpack in data.splitlines():
        half_a = set(backpack[:len(backpack)//2])
        half_b = set(backpack[len(backpack)//2:])
        ascii_item = ord(half_a.intersection(half_b).pop())
        item_value = ascii_item-96 if ascii_item > 90 else ascii_item-38
        total_points += item_value
    return total_points

def calculate_total_group_item_points(data:str):
    total_points = 0
    lines = data.splitlines()
    for backpack_group in (lines[i:i + 3] for i in range(0, len(lines), 3)):
        sets = [set(backpack) for backpack in backpack_group]
        ascii_item = ord(set.intersection(*sets).pop())
        item_value = ascii_item-96 if ascii_item > 90 else ascii_item-38
        total_points += item_value
    return total_points

if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR)

    total_points = calculate_total_item_points(data)
    assert(total_points==7581)
    submit(total_points,"a",day=DAY,year=YEAR)

    total_group_points = calculate_total_group_item_points(data)
    assert(total_group_points==2525)
    submit(total_group_points,"b",day=DAY,year=YEAR)
