from dotenv import load_dotenv
from aocd import get_data,submit

load_dotenv()
YEAR=2022
DAY=4
 

def check_overlaps(section_pair:str,strict:bool):
    ranges = [[int(item) for item in section.split("-")] for section in section_pair.split(",")]
    if strict:
        if (ranges[0][0]>=ranges[1][0] and ranges[0][1]<=ranges[1][1]) or (ranges[1][0]>=ranges[0][0] and ranges[1][1]<=ranges[0][1]):
            return 1
    elif (ranges[0][0]>=ranges[1][0] and ranges[0][0]<=ranges[1][1]) or (ranges[1][0]>=ranges[0][0] and ranges[1][0]<=ranges[0][1]):
        return 1
    return 0

def compute_total_set_overlaps(data:str,strict:bool):
    n_overlaps=0
    for section_pair in data.splitlines():
        n_overlaps+=check_overlaps(section_pair,strict)
    return n_overlaps


if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR)

    n_overlaps = compute_total_set_overlaps(data,True)
    assert(n_overlaps==580)
    submit(n_overlaps,"a",day=DAY,year=YEAR)

    n_overlaps = compute_total_set_overlaps(data,False)
    assert(n_overlaps==895)
    submit(n_overlaps,"b",day=DAY,year=YEAR)
