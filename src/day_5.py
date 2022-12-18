import re
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

def move(matrix,operations):
    for n,source,target in parse_operations(operations):
        matrix[target-1].extend(matrix[source-1][-1:-n-1:-1])
        del matrix[source-1][-1:-n-1:-1]
    return matrix

def get_first_chars(matrix):
    return "".join([row[-1] for row in matrix])

if __name__ == "__main__":
    data = get_data(day=DAY, year=YEAR).splitlines()
    index = data.index("")

    matrix = parse_matrix(data[:index])

    print(matrix)

    operations = data[index+1:]
    matrix = move(matrix,operations)
    result = get_first_chars(matrix)

    assert(result=="JDTMRWCQJ")
    submit(result,"a",day=DAY,year=YEAR)
    

    