import numpy as np

# Create two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
addition = A + B
print("\nAddition (A + B):")
print(addition)

# Matrix Multiplication
multiplication = np.dot(A, B)
print("\nMultiplication (A x B):")
print(multiplication)

# Transpose of a matrix
transpose_A = A.T
print("\nTranspose of Matrix A:")
print(transpose_A)
