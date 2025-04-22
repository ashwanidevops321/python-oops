import numpy as np

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

result_add = np.add(matrix_a, matrix_b)
result_subtract = np.subtract(matrix_a, matrix_b)
result_multiply = np.multiply(matrix_a, matrix_b)
    

print("Addition Result:")
print(result_add)

print("\nSubtraction Result:")
print(result_subtract)

print("\nMultiplication Result:")
print(result_multiply)