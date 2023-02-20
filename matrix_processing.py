import numpy as np
import numpy.random as rand


def matrix_input():
    try:
        n = int(input("Введите кол-во строк в матрице: "))
        m = int(input("Введите ко-во столбцов в матрице: "))

        if n == m or n == 0 or m == 0:
            print("Это не прямоугольная или некорректная матрица. Попробуйте еще раз.")
            matrix_input()
        return rand.randint(0, 10, (n, m)), n, m
    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте еще раз.")
        matrix_input()


def zero_search(matrix, n, m):
    try:
        l = int(input("Введите кол-во верхних строк в матрице, в которых будем искать нулевые элементы: "))
        k = int(input("Введите кол-во левых столбцов в матрице, в которых будем искать нулевые элементы: "))

        if (l > n or k > m) or (l == 0 or k == 0):
            print("Одно из введеных значений l или k превышают размер матрицы или равны 0. Попробуйте еще раз")
            zero_search(matrix, n, m)
        zero_counter = 0
        for i in range(l):
            for j in range(k):
                if matrix[i][j] == 0:
                    zero_counter += 1
        return zero_counter
    except ValueError:
        print("Вы ввели некорректное значение. Попробуйте еще раз.")
        zero_search(matrix, n, m)
