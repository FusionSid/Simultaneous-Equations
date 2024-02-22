import numpy as np

size = int(input("How many unknowns are there? "))
print(
    "Enter the coefficients and constants separated by spaces, with each equation separated by a new line:"
)

coefficients = []
answers = []

for i in range(size):
    equation = list(map(float, input().split()))
    if len(equation) != size + 1:
        raise ValueError("Invalid input provided")
    answers.append(equation.pop())
    coefficients.append(equation)

coefficients = np.array(coefficients)
answers = np.array(answers)

determinant = round(np.linalg.det(coefficients), 2)
print("Determinant of coefficients matrix:", determinant)

if determinant == 0:
    print("The system has either no solution or infinite solutions.")
    exit(0)

for unknown in range(size):
    mat = coefficients.copy()
    mat[:, unknown] = answers
    det_unknown = round(np.linalg.det(mat), 2)
    unknown_value = det_unknown / determinant
    print(f"Value of unknown {unknown + 1}: {unknown_value}")
