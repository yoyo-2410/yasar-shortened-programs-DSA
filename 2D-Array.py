import numpy as np

r1, c1 = map(int, input("Enter rows and cols of Matrix 1: ").split())
r2, c2 = map(int, input("Enter rows and cols of Matrix 2: ").split())

print("Enter Matrix 1:")
mat1 = np.array([list(map(float, input().split())) for _ in range(r1)])
print("Enter Matrix 2:")
mat2 = np.array([list(map(float, input().split())) for _ in range(r2)])

if r1 == r2 and c1 == c2:
    print("\nAddition:\n", mat1 + mat2)
    print("Subtraction:\n", mat1 - mat2)
else:
    print("\nAddition/Subtraction not possible.")

if c1 == r2:
    print("\nMultiplication:\n", np.dot(mat1, mat2))
else:
    print("\nMultiplication not possible.")

scalar = float(input("\nEnter scalar value: "))
print("\nScaling:\n", mat1 * scalar)
