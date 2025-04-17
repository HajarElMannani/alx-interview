#!/usr/bin/python3
'''
Pascal triangle
'''

def pascal_triangle(n):
    '''Return Pascal triangle'''
    triangle = []

    if n <= 0:
        return triangle

    for j in range(n):
        if j == 0:
            triangle.append([1])
        else:
            prev_row = triangle[-1]
            new_row = [1]

            for i in range(1, len(prev_row)):
                new_row.append(prev_row[i - 1] + prev_row[i])

            new_row.append(1)
            triangle.append(new_row)

    return triangle
