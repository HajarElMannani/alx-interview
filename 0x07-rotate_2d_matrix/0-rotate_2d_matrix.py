#!/usr/bin/python3
"""Rotate a 2D matrix"""


def rotate_2d_matrix(matrix):
    """function to rotate a matric clockwise"""
    length = len(matrix)

    for i in range(length):
        for j in range(i + 1, length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
