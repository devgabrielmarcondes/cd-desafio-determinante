from itertools import permutations

matrix = []
row = int(input("Number of lines: "))
col = int(input("Number of columns: "))

def new_matrix():
    for r in range(row):
        matrix.append([])
        for c in range(col):
            value = int(input(f"Value at row {r+1}, column {c+1}: "))
            matrix[r].append(value)
    return matrix
new_matrix()

def view_matrix():
    print(f"\nThe {row}x{col} matrix is: ")
    for r in range(row):
        for c in range(col):
            print(f"[{matrix[r][c]}]", end='')
        print()
view_matrix()

def determinant(matrix):
    n = len(matrix)
    if n != len(matrix[0]):
        print("The matrix must be square.")
        return None
    else:
        det = 0
        for perm in permutations(range(n)):
            diag = 1
            for i in range(n):
                diag *= matrix[i][perm[i]] # diagonal of the matrix
            det += (-1)**sum((perm[j] > perm[i]) for i in range(n) for j in range(i+1, n)) * diag
        return det

print(f"\n det(A) = {determinant(matrix)}")


