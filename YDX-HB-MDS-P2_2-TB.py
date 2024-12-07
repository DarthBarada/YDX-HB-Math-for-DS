import pytest
"""
*---------------------------*----------------------------------------*
|    Ограничение времени    |    2 секунды                           |
|    Ограничение памяти     |    64Mb                                |
|    Ввод                   |    стандартный ввод или input.txt      |
|    Вывод                  |    стандартный вывод или output.txt    |
*---------------------------*----------------------------------------*

Дан ориентированный граф, заданный матрицей смежности размером N × N. 

Ваша задача — преобразовать этот граф в список смежности.

# Формат входных данных
В первой строке дано целое число N — количество вершин в графе ( 1 ≤ N ≤ 1000). 

Далее следуют N строк по N чисел: j-е число в i-й строке равно 1, если существует ребро между вершинами i и j, и 0 иначе.

# Формат выходных данных
Выведите N строк. В i-й строке выведите через пробел номера вершин в котрые есть ребро из врешины i. Если из вершины i нет исходящих рёбер, оставьте строчку пустой.
"""
def test_example(capsys):
    assert processInput(
        3,
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0],
        ]
    ) == "1\n2\n0"
    
    assert processInput(
        2,
        [
            [0, 1],
            [0, 0],
        ]
    ) == "1\n"
    
    assert processInput(
        3,
        [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
    ) == "\n\n"
    
    assert processInput(
        4,
        [
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0],
        ]
    ) == "1 3\n2\n3\n"


def processMatrix(amount:int, mat: list[list[int]]) -> list[list[int]]:
    res:list[list[int]] = []
    for row in range(amount):
        res.append([])
        for col in range(amount):
            if mat[row][col] == 1:
                res[row].append(col)
    
    return res


def processInput(amount:int, mat: list[list[int]]) -> str:
    return "\n".join(
        [
            " ".join(
                map(str, row)
            ) 
            for row in processMatrix(amount, mat)
        ]
    )


def main():
    import sys
    amount = int(input())
    mat = [list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(amount)]
    print(processInput(amount, mat))


if __name__ == '__main__':
    main()
