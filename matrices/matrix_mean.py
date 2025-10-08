import numpy as np


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "column":
        return np.array(matrix).mean(0)
    elif mode == "row":
        return np.array(matrix).mean(1)
    else:
        raise RuntimeError
