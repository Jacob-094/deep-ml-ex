import numpy as np


def scalar_multiply(
    matrix: list[list[int | float]], scalar: int | float
) -> list[list[int | float]]:
    A = np.array(matrix)

    return A * scalar
