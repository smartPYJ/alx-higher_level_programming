#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    for key, value in a_dictionary.items():
        keys.append(key)
    keys.sort()

    for i in keys:
	print(str(i)+": "+str(a_dictionary.get(i)))
