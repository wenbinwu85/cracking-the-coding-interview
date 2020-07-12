# rotate matrix counterclockwise
def rotate_matrix(matrix: list) -> list:
    n = len(matrix)
    rotated = []
    for i in range(n):
        new_row = [matrix[j][n-i-1] for j in range(n)]
        rotated.append(new_row)
    return rotated


# rotate matrix clockwise
def rotate_matrix2(matrix: list) -> list:
    n = len(matrix)
    rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = matrix[i][j]
    return rotated

# to be continued...
def rotate_matrix_in_place(matrix: list) -> None:
    pass


def print_matrix(matrix: list) -> None:
    for row in matrix:
        for column in row:
            print(column, end=' ')
        print()


if __name__ == '__main__':
    matrix1 = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
        ]
        
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ]

    rotated = rotate_matrix2(matrix1)
    print_matrix(matrix1)
    print()
    print_matrix(rotated)
    
    print()
    
    rotated = rotate_matrix2(matrix2)
    print_matrix(matrix2)
    print()
    print_matrix(rotated)
