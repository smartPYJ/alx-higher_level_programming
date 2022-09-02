#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        if len(i) == 0:
            return 0
        else:
            for j in i:
                newlist = [j*j for j in i]
            new.append(newlist)
    return new
