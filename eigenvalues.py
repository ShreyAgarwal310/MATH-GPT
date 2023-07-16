import numpy as np

def find_eigenvalues(matrix):
    eigenvalues, _ = np.linalg.eig(matrix)
    return eigenvalues

matrix = np.array([[2, -1], [4, 3]])
eigenvalues = find_eigenvalues(matrix)
print("Eigenvalues:", eigenvalues)