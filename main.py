from matrix_processing import matrix_input, zero_search

if __name__ == '__main__':
    matrix, n, m = matrix_input()
    print(f"Матрица:\n {matrix}")
    ans = zero_search(matrix, n, m)
    print(f"Кол-во нулевых элементов в матрице {ans}")
