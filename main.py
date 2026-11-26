
import numpy as np

print("===== NUMPY VECTOR CALCULATIONS =====")

# 1. Create one-dimensional arrays
a = np.array([10, 20, 30, 40])
b = np.array([5, 10, 15, 20])

print("\n1. NumPy Arrays")
print("Array A:", a)
print("Array B:", b)

# 2. Vector calculations
print("\n2. Vector Operations")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 3. Dot product
print("\n3. Dot Product")
dot_product = np.dot(a, b)
print("Dot Product:", dot_product)

# 4. Two-dimensional arrays
print("\n4. Two-Dimensional Arrays")
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", matrix_a)
print("Matrix B:\n", matrix_b)

# 5. Matrix operations
print("\n5. Matrix Operations")
print("Matrix Addition:\n", matrix_a + matrix_b)
print("Matrix Multiplication:\n", np.dot(matrix_a, matrix_b))
print("Transpose of Matrix A:\n", matrix_a.T)

# 6. Linear algebra transformations
print("\n6. Linear Algebra")
print("Determinant:", np.linalg.det(matrix_a))
print("Inverse:\n", np.linalg.inv(matrix_a))

# 7. Multi-dimensional arrays
print("\n7. Multi-Dimensional Arrays")
array_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("3D Array:\n", array_3d)
print("Array Shape:", array_3d.shape)
print("Number of Dimensions:", array_3d.ndim)
print("Total Elements:", array_3d.size)

# 8. Array statistics
print("\n8. Array Statistics")
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))
print("Sum:", np.sum(a))

print("\n===== PROJECT COMPLETED SUCCESSFULLY =====")
