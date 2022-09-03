#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        new = list(a_dictionary.values())
        new.sort()
        for key, value in a_dictionary.items():
            if new[-1] == value:
                return key
            else:
                continue
