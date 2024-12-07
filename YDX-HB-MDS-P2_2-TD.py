import queue
import pytest
"""
*---------------------------*----------------------------------------*
|    Ограничение времени    |    2 секунды                           |
|    Ограничение памяти     |    64Mb                                |
|    Ввод                   |    стандартный ввод или input.txt      |
|    Вывод                  |    стандартный вывод или output.txt    |
*---------------------------*----------------------------------------*

Дан неориентированный невзвешенный граф, представленный матрицей смежности размером N × N. Также заданы индексы двух различных вершин S и T. Требуется найти длину кратчайшего пути между вершинами S и T.

Ваша задача — преобразовать этот граф в список смежности.

# Формат входных данных
В первой строке дано целое число N — количество вершин в графе ( 1 ≤ N ≤ 500). 

Далее следуют N строк по N чисел: j-е число в i-й строке равно 1, если существует ребро между вершинами i и j, и 0 иначе.

В последней строке заданы два целых числа S и T - индексы начальной и конечной вершин (0 ≤ S,T < N, S ≠ T) 

# Формат выходных данных
Выведите одно число — длину кратчайшего пути между вершинами S и T. Если пути не существует, выведите -1.
"""
def test_example(capsys):
    assert processInput(
        0,
        3,
        [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
        ]
    ) == "3"
    
    assert processInput(
        0,
        3,
        [
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
        ]
    ) == "3"
    
    assert processInput(
        0,
        3,
        [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [0, 0, 1, 1, 0],
        ]
    ) == "3"
    
    assert processInput(
        0,
        3,
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    ) == "-1"
    
    assert processInput(
        0,
        5,
        [
            [0, 1, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1],
            [0, 0, 0, 1, 1, 0],
        ]
    ) == "3"


def getPath(
    start: int,
    end: int,
    path: list[int],
    mat: list[list[int]]
) -> list[list[int]]:
    paths:list[list[int]] = []
    for col in range(len(mat[start])):
        ver = mat[start][col]
        if col in path or ver == 0:
            continue
        newPath = path.copy()
        newPath.append(col)
        if col == end:
            paths.append(newPath)
        else:
            resArr = getPath(
                col,
                end,
                newPath,
                mat
            )
            if len(resArr) > 0:
                paths.extend(resArr)

    return paths
    
    
def processMatrix(
    start: int,
    end: int,
    mat: list[list[int]]
) -> int:
    res = getPath(start, end, [start], mat)
    if len(res) == 0 :
        return -1
    else:
        return len(min(res, key=lambda x: len(x))) - 1


def processInput(
    start: int,
    end: int,
    mat: list[list[int]]
) -> str:
    return str(processMatrix(start, end, mat))


def main():
    import sys
    amount = int(input())
    mat = [list(map(int,sys.stdin.readline().rstrip("\n").split())) for _ in range(amount)]
    start, end = list(map(int, input().split()))
    print(processInput(start, end, mat))


if __name__ == '__main__':
    main()
