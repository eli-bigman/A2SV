def non_zero_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                return [i+1,j+1]


matrix = [list(map(int, input().split())) for _ in range(5)]

i, j = non_zero_position(matrix)

print(abs((i - 3 )) + abs((j - 3)))

