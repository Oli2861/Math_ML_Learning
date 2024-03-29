import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


def plot_vectors(*vector_name: Tuple[np.ndarray, str]):
    labels = []
    for vn in vector_name:
        vector, name = vn
        xs = [0, vector[0]]
        ys = [0, vector[1]]
        plt.plot(xs, ys)
        labels.append(name)
    plt.xlim([-10, 10])
    plt.ylim([-10, 10])
    plt.legend(labels)
    plt.show()


def pretty_print_matrix(matrix, label: str = None, max_length: int = 1):
    if label is not None:
        print(label)
    print("[")
    for row in matrix:
        print("  ", end="")
        if isinstance(row, np.ndarray) or isinstance(row, list):
            for entry in row:
                print(f"{entry:^{max_length}}", end=" ")
        else:
            print(row, end=" ")
        print()
    print("]")
