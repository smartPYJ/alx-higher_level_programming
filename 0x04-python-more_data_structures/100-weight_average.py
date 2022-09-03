#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    sum_up = [x[0] * x[1] for x in my_list]
    divide = [x[1] for x in my_list]
    average = sum(sum_up) / sum(divide)
    return average
