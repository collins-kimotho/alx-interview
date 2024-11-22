#!/usr/bin/python3
"""
Rotate 2D Matrix Module
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The n x n 2D matrix to rotate.
    """
    # Step 1: Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to complete the rotation
    for row in matrix:
        row.reverse()
