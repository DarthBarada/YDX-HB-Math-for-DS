import pytest
"""
*---------------------------*----------------------------------------*
|    Ограничение времени    |    2 секунды                           |
|    Ограничение памяти     |    64Mb                                |
|    Ввод                   |    стандартный ввод или input.txt      |
|    Вывод                  |    стандартный вывод или output.txt    |
*---------------------------*----------------------------------------*

Вам дан неориентированный граф, представленный в виде матрицы смежности размером N × N, где N — количество вершин в графе. Вершины пронумерованы от 0 до N − 1. 

Ваша задача — вывести индексы вершин, на которых есть петли (то есть ребра, соединяющие вершину саму с собой).

# Формат входных данных
В первой строке дано целое число N — количество вершин в графе ( 1 ≤ N ≤ 1000). 

Далее следуют N строк по N чисел: j-е число в i-й строке равно 1, если существует ребро между вершинами i и j, и 0 иначе.

# Формат выходных данных
Выведите в порядке возрастания индексы вершин, на которых есть петли. Если таких вершин нет, выведите строку NO LOOPS.
"""
def test_example():
    assert processInput(
        4,
        [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 1],
        ]
    ) == "1\n3"
    
    assert processInput(
        3,
        [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 0]
        ]
    ) == "0"
    
    assert processInput(
        4,
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    ) == "NO LOOPS"
    
    assert processInput(
        5,
        [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1],
        ]
    ) == "0\n1\n2\n3\n4"


def processMatrix(amount:int, mat: list[list[int]]) -> list[int]:
    res:list[int] = []
    for idx in range(amount):
        if mat[idx][idx] == 1:
            res.append(idx)
    
    return res


def processInput(amount:int, mat: list[list[int]]) -> str:
    res = processMatrix(amount, mat)
    if len(res) == 0:
        return "NO LOOPS"
    else:
        return "\n".join(map(str,res))


def main():
    import sys
    amount = int(input())
    mat = [list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(amount)]
    print(processInput(amount, mat))


if __name__ == '__main__':
    main()
