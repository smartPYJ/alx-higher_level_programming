#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new = my_list[::-1]
    for i in range(0, len(new)):
        print("{}".format(new[i]))
