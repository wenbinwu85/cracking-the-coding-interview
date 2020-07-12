def zero_matrix(matrix: list) -> list:
    m = len(matrix)
    cols = []
    for row in matrix:
        for j in range(len(row)):
            if row[j] == 0 and (j not in cols):
                cols.append(j)

    for i in range(m):
        row = matrix[i]
        if 0 in row:
            row = [0] * len(row)
        else:
            for j in cols:
                row[j] = 0
        matrix[i] = row


def print_matrix(matrix: list) -> None:
    for row in matrix:
        for column in row:
            print(column, end=' ')
        print()           


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4, 11],
        [5, 6, 7, 0, 12],
        [7, 8, 0, 10, 13],
    ]

    print_matrix(matrix)
    zero_matrix(matrix)
    print()
    print_matrix(matrix)
