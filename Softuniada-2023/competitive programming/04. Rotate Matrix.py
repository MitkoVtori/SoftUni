from collections import deque


def flip_matrix(matrix):
    global size

    flipped_matrix = []

    for col in range(size):
        flipped_row = deque()

        for row in range(size):
            flipped_row.appendleft(matrix[row][col])

        flipped_matrix.append(list(flipped_row))

    return '\n'.join([' '.join([str(col) for col in row]) for row in flipped_matrix])


size = int(input())

matrix = []

for row in range(size):
    columns = list(map(int, input().split()))
    matrix.append(columns)

print(flip_matrix(matrix))
