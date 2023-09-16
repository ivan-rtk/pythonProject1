# Напишите функцию для транспонирования матрицы
def trans_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    trans = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            trans[j][i] = matrix[i][j]
    return trans


original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in original_matrix:
    print(row)
print()
trans_matrix = trans_matrix(original_matrix)
for row in trans_matrix:
    print(row)