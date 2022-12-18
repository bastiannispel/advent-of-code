import re
from copy import deepcopy
from dotenv import load_dotenv
from aocd import get_data,submit

load_dotenv()
YEAR=2022
DAY=5
 
def print_matrix(matrix):
    for row in matrix:
        print(row)

def parse_matrix(data:str):
    n_cols = (len(data[0])+1)//4
    matrix=[[] for _ in range(n_cols)]
    n_rows = len(data)-1
    for n_row in range(n_rows):
        for i,item in enumerate(data[n_row][1::4]):
            if item != " ":
                matrix[i].append(item)
    matrix = [row[::-1] for row in matrix]
    return matrix

def parse_operations(operations):
    for operation in operations:
        yield [int(op) for op in re.findall("\d+",operation)]

def move(matrix,operations,multi_crates):
    temp_matrix = deepcopy(matrix)
    for n,source,target in parse_operations(operations):
        length_source = len(temp_matrix[source-1])
        crates = slice(length_source-n,length_source) if multi_crates else slice(-1,-n-1,-1)
        temp_matrix[target-1].extend(temp_matrix[source-1][crates])
        del temp_matrix[source-1][crates]
    return temp_matrix

def get_first_chars(matrix):
    return "".join([row[-1] for row in matrix])

if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).splitlines()
    index = data.index("")

    matrix = parse_matrix(data[:index])
    operations = data[index+1:]

    matrix_crane_9000 = move(matrix,operations,False)
    result_part_a = get_first_chars(matrix_crane_9000)
    assert(result_part_a=="JDTMRWCQJ")
    submit(result_part_a,"a",day=DAY,year=YEAR)

    print_matrix(matrix)
    print()
    matrix_crane_9001 = move(matrix,operations,True)
    result_part_b = get_first_chars(matrix_crane_9001)
    assert(result_part_b=="VHJDDCWRD")
    submit(result_part_b,"b",day=DAY,year=YEAR)
    

    